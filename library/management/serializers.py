from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    uri = serializers.HyperlinkedIdentityField(view_name='author-detail', read_only=True)

    class Meta:
        model = Author
        fields = ['name','uri']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', read_only=True)
    uri = serializers.HyperlinkedIdentityField(view_name='book-detail', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    uri = serializers.HyperlinkedIdentityField(view_name='member-detail', read_only=True)
    class Meta:
        model = Member
        fields = ['name', 'uri']

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