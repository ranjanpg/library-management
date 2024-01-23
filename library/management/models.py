from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=200)
    finesAccrued = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    EXPIRATION_DAYS = 20

    class Status(models.IntegerChoices):
        ACTIVE = 1
        PENDING = 2
        CANCELLED = 3
        CHECKED_OUT = 4

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reservations')
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices = Status.choices, default=1)

    def checkExpired(self):
        return self.status == Reservation.Status.CHECKED_OUT
    
    def cancel(self):
        self.status = Reservation.Status.CANCELLED
        self.save()

    def __str__(self) -> str:
        return f"Reservation - {self.book}::{self.member} at {self.createdAt} :: status::{self.get_status_display()}"

class Checkout(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='checkoutDetails')
    createdAt = models.DateTimeField(auto_now_add=True)

    def clean(self) -> None:
        self.reservation.status = Reservation.Status.CHECKED_OUT
        return super().clean()