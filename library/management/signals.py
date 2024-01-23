from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Reservation, Checkout

@receiver(post_save, sender=Checkout)
def checkoutHandler(sender, instance, created, **kwargs):
    if created:
        reservation = instance.reservation
        reservation.status = Reservation.Status.CHECKED_OUT
        reservation.save()
        reservation.book.count += 1