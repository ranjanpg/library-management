from rest_framework import serializers
from .models import *

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name']

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    createdAt = serializers.DateTimeField()

    class Meta:
        model = Reservation
        fields = ['member', 'book', 'createdAt', 'status']

class CheckoutSerializer(serializers.HyperlinkedModelSerializer):
    reservation = ReservationSerializer()
    createdAt = serializers.DateTimeField()

    class Meta:
        model = Checkout
        fields = ['reservation', 'createdAt']