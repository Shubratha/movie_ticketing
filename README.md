# movie_ticketing
APIs for movie ticketing website

### APIs:
- User signup
- View all movies playing in a city
- View all cinemas that is playing a movie
- Check seat availability for a movie show
- Book a show ticket

### Setup:
1. **Prerequisites:** python3
2. Clone repo
3. Install requirements given in requirements.txt
   ```commandline
   pip install -r requirements.txt
   ```
4. Import database
   ```commandline
   cd movie_booking_site
   python manage.py migrate
   cat movie_ticketing.sql | sqlite3 movie_ticketing.db
   ```
5. Run app
   ```commandline
   python manage.py runserver
   ```
6. Try out the APIs :cowboy_hat_face:

#### Apps capable of being separate microservice:
- Inventory [^1](https://github.com/Shubratha/movie_ticketing/tree/main/movie_booking_site/inventory#readme)
- Booking [^2](https://github.com/Shubratha/movie_ticketing/tree/main/movie_booking_site/user#readme)
- User/Auth [^3](https://github.com/Shubratha/movie_ticketing/tree/main/movie_booking_site/booking#readme)


[Hosted Website- Live Try](https://shubratha.pythonanywhere.com/cinemas/getMovies/Bangalore/)

[Postman Collection](https://www.getpostman.com/collections/65844f140b26afd91095)
