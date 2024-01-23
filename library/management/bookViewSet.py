from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Reservation
from django.db.models import Count
from .serializers import BookSerializer, ReservationSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(methods=['GET'], detail=True)
    def reservations(self, request, *args, **kwargs):
        obj = self.get_object()
        reservations = obj.reservations.all()
        serializer = ReservationSerializer(reservations, many=True, context={'request': request})
        return Response(data=serializer.data)
    
    @action(detail=False, methods=['GET'])
    def mostPopularBooks(self, request, *args, **kwargs):
        most_popular_books = Reservation.objects.values('book__title', 'book__author', 'book__id').annotate(reservation_count=Count('id')).order_by('-reservation_count')
        return Response(data= most_popular_books)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)