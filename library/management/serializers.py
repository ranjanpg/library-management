from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='author-detail', read_only=True)

    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    uri = serializers.HyperlinkedIdentityField(view_name='member-detail', read_only=True)
    class Meta:
        model = Member
        fields = '__all__'

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Reservation
        fields = '__all__'

class CheckoutSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Checkout
        fields = '__all__'