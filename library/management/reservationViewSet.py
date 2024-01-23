from rest_framework import viewsets
from rest_framework.response import Response
from .models import Reservation, Checkout
from .serializers import ReservationSerializer, CheckoutSerializer
from rest_framework.decorators import action
from .utils import url_to_object
from collections import defaultdict
from datetime import datetime, timezone

FINE_RATE_PER_DAY = 50

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    reservationQueue = defaultdict(list)

    def create(self, request, *args, **kwargs):
        book = url_to_object(request.data['book'])
        member = url_to_object(request.data['member'])
        if Reservation.objects.filter(book=book, member=member, status=Reservation.Status.ACTIVE).exists():
            return Response(data="Same issue not allowed!")
        
        if book.reservations.filter(status=Reservation.Status.ACTIVE).exists():
            ReservationViewSet.reservationQueue[book.title].append(member)
            return Response(data="Book not available!")

        return super().create(request, *args, **kwargs)
    
    @action(methods=['POST'], detail=True)
    def cancel(self, request, *args, pk, **kwargs):
        obj = self.get_object()
        if obj.status == Reservation.Status.PENDING:
            obj.status = Reservation.Status.CANCELLED
            obj.save()
            return Response(data="Reservation Cancelled!")
        return Response(data="No Reservation Present!")

    # @action(methods=['POST'], detail=True)
    # def checkout(self, request, *args, pk, **kwargs):
    #     obj = self.get_object()
    #     if obj.status != Reservation.Status.ACTIVE:
    #         return Response("Only active reservations can be checked out!")
    #     obj.status = Reservation.Status.CHECKED_OUT

    #     return Response(data="No Reservation Present!")

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def create(self, request, *args, **kwargs):
        reservation = url_to_object(request.data['reservation'])
        if reservation.status != Reservation.Status.ACTIVE:
            return Response("Only active reservations can be checked out!")
        ret = super().create(request, *args, **kwargs)
        if ret.status_code == 201:
            book = reservation.book
            fine = None
            try:
                fine = self.calculateFine(reservation, ret.data.get('createdAt'))
            except Exception as e:
                print(e)
            if fine > 0:
                reservation.member.finesAccrued += fine
                reservation.member.save()
            waitingQueue = ReservationViewSet.reservationQueue[book.title]
            if len(waitingQueue):
                firstRequester = waitingQueue.pop(0)
                r = Reservation.objects.create(member=firstRequester, book=book)
                r.save()
            reservation.status = Reservation.Status.CHECKED_OUT
        return ret
    
    def calculateFine(self, reservationObj, currentTime):
        timedelta = datetime.fromisoformat(currentTime).replace(tzinfo=timezone.utc) - reservationObj.createdAt
        daysBorrowed = timedelta.days
        if daysBorrowed <= Reservation.EXPIRATION_DAYS:
            return 0
        return (daysBorrowed - Reservation.EXPIRATION_DAYS) * FINE_RATE_PER_DAY
