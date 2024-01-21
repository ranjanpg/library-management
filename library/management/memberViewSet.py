from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer, ReservationSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(methods=['GET'], detail=True)
    def reservations(self, request, *args, pk, **kwargs):
        member = self.get_object()
        status = 1 if request.query_params.get('active') else 2
        reservations = member.reservations.filter(status=status)
        if pk:
            reservations = reservations.filter(pk=pk)
        data = [ReservationSerializer(reservation, context={'request': request}).data for reservation in reservations]
        return Response(data=data)
