import json
import logging
from datetime import datetime

from django.http import HttpResponse
from rest_framework.views import APIView

from .models import City, Seat, Show

logger = logging.getLogger(__name__)


class GetAllCities(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Returns movies playing in the city
        """
        response = {"status": False, "cities": [], "error": ""}

        try:

            city_objs = City.objects.all()
            logger.info("city_objs: %s" % city_objs)
            cities = []

            for city in city_objs:
                cities.append(city.name)

            response.update({"status": True, "cities": cities})

        except Exception as e:
            logger.critical("Exception in GetAllCities: %s" % str(e))
            response.update({"error": str(e)})

        return HttpResponse(json.dumps(response), content_type="application/json")


class GetMoviesByCity(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, city):
        """
        Returns movies playing in the city
        """
        response = {"status": False, "movies": [], "error": ""}

        try:

            show_objs = Show.objects.filter(theatre__fk_city__name=city)
            logger.info("shows: %s" % show_objs)
            movies = []

            for show in show_objs:
                movies.append({"show_id": show.id, "movie_name": show.movie.name})

            response.update({"status": True, "movies": movies})

        except Exception as e:
            logger.critical("Exception in GetMoviesByCity: %s" % str(e))
            response.update({"error": str(e)})

        return HttpResponse(json.dumps(response), content_type="application/json")


class GetTheatreByMovie(APIView):
    """
    Returns cinemas/theatres playing requested movie
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, movie):

        response = {"status": False, "cinemas": [], "error": ""}
        try:

            if not movie:
                response.update({"error": "Movie name not found"})
                return HttpResponse(json.dumps(response), status=400)

            show_objs = Show.objects.filter(movie__name=movie)
            theatres = []

            for show in show_objs:
                theatres.append(
                    {
                        "name": show.theatre.name,
                        "timing": datetime.strftime(show.timing, "%d %B, %H:%M"),
                        "screen": show.screen,
                        "show_id": show.id,
                    }
                )
            response.update({"cinemas": theatres})

        except Exception as e:
            logger.critical("Exception in GetMoviesByCity: %s" % str(e))
            response.update({"error": str(e)})

        return HttpResponse(json.dumps(response), content_type="application/json")


class GetSeatAvailability(APIView):
    """
    Returns available seats for a requested show
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, show_id):
        response = {
            "status": False,
            "seats": [],
            "error": "",
            "message": "HouseFull, No seats available",
        }
        try:
            show_time = ""
            if not show_id:
                response.update({"error": "Invalid show"})
                return HttpResponse(json.dumps(response), status=400)

            seat_objs = Seat.objects.filter(show__id=show_id, is_available=True)
            seats = []

            for seat in seat_objs:
                seats.append(seat.number)
                show_time = datetime.strftime(seat.show.timing, "%d %B, %H:%M")
                response.update(
                    {
                        "status": True,
                        "show_time": show_time,
                        "total_available_seats": len(seat_objs),
                        "seats": seats,
                        "message": "%s seat(s) available" % len(seat_objs),
                    }
                )

        except Exception as e:
            logger.critical("Exception in GetMoviesByCity: %s" % str(e))
            response.update({"error": str(e)})

        return HttpResponse(json.dumps(response), content_type="application/json")
