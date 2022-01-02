from django.contrib import admin

from . import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):

    list_display = ("id", "name")


@admin.register(models.Theatre)
class TheatreAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "fk_city", "total_screens")


@admin.register(models.Show)
class ShowAdmin(admin.ModelAdmin):

    list_display = ("id", "movie", "theatre", "screen")


@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):

    list_display = ("id", "number", "show")


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "image", "language")
