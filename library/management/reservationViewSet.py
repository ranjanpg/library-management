from rest_framework import viewsets
from rest_framework.response import Response
from .models import Reservation, Checkout
from .serializers import ReservationSerializer, CheckoutSerializer
from rest_framework.decorators import action

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @action(methods=['POST'], detail=True)
    def cancel(self, request, *args, pk, **kwargs):
        obj = self.get_object()
        if obj.status == 1:
            obj.status = 2
            return Response(data="Reservation Cancelled!")
        return Response(data="No Reservation Present!")

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
