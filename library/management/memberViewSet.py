from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Member, Reservation
from .serializers import MemberSerializer, ReservationSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(methods=['GET'], detail=True)
    def reservations(self, request, *args, **kwargs):
        obj = self.get_object()
        reservations = obj.reservations.all()
        query = request.query_params.get('status', None)
        if query:
            status = Reservation.Status[query.upper()]
            reservations = reservations.filter(status=status)
        serializer = ReservationSerializer(reservations, many=True, context={'request': request})
        return Response(data=serializer.data)
