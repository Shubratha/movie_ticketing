from django.contrib.auth.models import User
from django.db import models
from inventory.models import Seat


class Booking(models.Model):
    booking_id = models.CharField(unique=True, max_length=200, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta(object):
        db_table = "booking"

    def __str__(self):
        return str(self.id)


class SeatBooked(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bookedSeats"
        unique_together = ("seat", "booking")
        verbose_name = "Booked Seat"

    def __str__(self):
        return str(self.seat) + "|" + str(self.booking)
