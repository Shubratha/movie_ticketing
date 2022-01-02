# Booking

- Stores booking related information.
- Provides endpoints to book tickets for a movie show.
- Available only to authenticated users

### Tables:
1. **Booking** - stores booking ID, user who has booked, amount paid
2. **SeatBooked** - stores seat booked, booking ID

###APIs:
1. Book Ticket

Accepts show id and seat numbers and returns booking ID
Authorization token to be provided- If token provided directly, then encode using base64 in `<username>:<password>` format.

```commandline
curl --location --request POST 'http://127.0.0.1:8000/book/ticket/' \
--header 'Authorization: Basic dmlnZ3k6cGlnZ3k=' \
--header 'Content-Type: application/json' \
--data-raw '{
    "show_id": 1,
    "seat_numbers": ["<seat_number>"]
}'
```

Sample Response:
```json
{
    "status": true,
    "message": "Booking successful, BookingID: <bookingID>"
}
```
