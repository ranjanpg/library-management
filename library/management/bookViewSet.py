from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
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

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)