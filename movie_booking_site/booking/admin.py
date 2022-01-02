from django.contrib import admin

from . import models


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ("id", "booking_id", "timestamp", "amount", "customer")


@admin.register(models.SeatBooked)
class SeatBooked(admin.ModelAdmin):

    list_display = ("id", "seat", "booking", "timestamp")
