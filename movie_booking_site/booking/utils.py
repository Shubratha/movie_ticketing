import logging
import uuid

from .models import Booking, SeatBooked

logger = logging.getLogger(__name__)


def generate_booking_id():
    return str(uuid.uuid4())


def create_booking(user_obj, seats):
    booking_id = generate_booking_id()
    try:
        booking = Booking.objects.create(booking_id=booking_id, customer=user_obj)

        seat_objs = []
        for seat in seats:
            seat.is_available = False
            seat.save()

            seat_obj = SeatBooked(seat=seat, booking=booking)
            seat_objs.append(seat_obj)

        logger.info(
            "Booking for user %s, Seats: %s, BookingId: %s"
            % (user_obj.username, len(seats), booking_id)
        )
        SeatBooked.objects.bulk_create(seat_objs)

    except Exception as e:
        logger.critical(
            "Exception in create_booking for BookingId %s:  %s" % (booking_id, str(e))
        )
        raise Exception(e)

    return booking_id
