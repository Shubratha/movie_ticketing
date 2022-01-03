from django.urls import include, path

from . import views

urlpatterns = [
    path("getMovies/<str:city>/", views.GetMoviesByCity.as_view()),
    path("getCinemas/<str:movie>/", views.GetTheatreByMovie.as_view()),
    path("getSeats/<str:show_id>/", views.GetSeatAvailability.as_view()),
    path("getCities/", views.GetAllCities.as_view()),
]
