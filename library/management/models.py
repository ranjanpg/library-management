from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Member(models.Model):
    name = models.CharField(max_length=200)

class Reservation(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 1
        CANCELLED = 2

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reservations')
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices = Status.choices, default=1)

class Checkout(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='checkoutDetails')
    createdAt = models.DateTimeField(auto_now_add=True)