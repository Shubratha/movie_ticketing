from django.urls import include, path

from . import views

urlpatterns = [path("ticket/", views.BookMovieTicket.as_view())]
