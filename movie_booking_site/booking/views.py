import logging

from inventory.models import Seat
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import create_booking

logger = logging.getLogger(__name__)


class BookMovieTicket(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        1. check show id and seats availability
        2. Update Seat is_available field for each seat
        3. create entry in Booking and SeatsBooked
        """
        response = {"status": False, "message": ""}
        try:

            data = request.data
            seat_numbers = data.get("seat_numbers", [])
            show_id = data.get("show_id")

            logger.info(
                "Booking initiated by user %s for show %s" % (request.user, show_id)
            )

            if not show_id:
                response.update({"message": "Invalid show selected"})
                return Response(response)

            if not seat_numbers:
                response.update({"message": "No seat selected"})
                return Response(response)

            # check for show id and seats availability
            seat_objs = Seat.objects.filter(
                show__id=show_id, number__in=seat_numbers, is_available=True
            )

            if len(seat_objs) == len(seat_numbers):
                # create booking records
                booking_id = create_booking(request.user, seat_objs)
                response.update(
                    {
                        "status": True,
                        "message": "Booking successful, BookingID: %s" % booking_id,
                    }
                )

            else:
                response.update({"message": "Not all selected seats available"})

        except Exception as e:
            logger.critical("Exception in BookMovieTicket: %s" % str(e))
            response.update({"message": str(e)})

        return Response(response)
