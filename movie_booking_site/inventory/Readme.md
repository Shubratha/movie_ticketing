# Inventory

Inventory has the basic details needed for the website. This app stores information about theatres available, movies playing and show details. It also supports APIs that can query these details to fetch required information.

### Tables:
1. City
2. Theatre
3. Movie
4. Show
5. Seat

The details can be added by admin using Admin Panel ([/admin](http://127.0.0.1:8000/admin/))

### API

These are public APIs i.e., no authentication required

**1. Get all cities available**
```
curl --location --request GET 'http://127.0.0.1:8000/cinemas/getCities/'
```
Sample Response:
```json
{
    "status": true,
    "error": "",
    "cities": [
        "Bangalore",
        "Hyderabad"
    ]
}
```

**2. Fetch movies playing in a city**
```
curl --location --request GET 'http://127.0.0.1:8000/cinemas/getMovies/<city_name>/'
```
Sample Response:
```json
{
    "status": true,
    "movies": [
        {
            "show_id": 1,
            "movie_name": "Spider-Man: Far from Home"
        },
        {
            "show_id": 3,
            "movie_name": "83"
        },
        {
            "show_id": 2,
            "movie_name": "Sing 2"
        }
    ],
    "error": ""
}
```


**3. Fetch all cinemas playing a movie**
```buildoutcfg
curl --location --request GET 'http://127.0.0.1:8000/cinemas/getCinemas/<movie_name>/'
```
Sample Response:
```json
{
    "status": false,
    "cinemas": [
        {
            "name": "PVR",
            "timing": "02 January, 12:15",
            "screen": 2,
            "show_id": 3
        },
        {
            "name": "Carnival",
            "timing": "02 January, 12:30",
            "screen": 1,
            "show_id": 4
        }
    ],
    "error": ""
}
```

**4. Check seats available for a movie show**
```commandline
curl --location --request GET 'http://127.0.0.1:8000/cinemas/getSeats/<show_id>/'
```
Sample Response:
```json
{
    "status": true,
    "seats": [
        "A0",
        "B1"
    ],
    "error": "",
    "message": "2 seat(s) available",
    "show_time": "02 January, 12:14",
    "total_available_seats": 2
}
```
```json
{
    "status": false,
    "seats": [],
    "error": "",
    "message": "HouseFull, No seats available"
}
```
