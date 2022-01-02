from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)

    class Meta(object):
        db_table = "city"
        # verbose_name = 'Citie'

    def __str__(self):
        return self.name


class Theatre(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    fk_city = models.ForeignKey(City, on_delete=models.CASCADE, db_index=True)
    total_screens = models.IntegerField(default=1)

    class Meta(object):
        db_table = "theatre"

    def __str__(self):
        return self.name


class Movie(models.Model):
    language_choices = (
        ("ENGLISH", "English"),
        ("HINDI", "Hindi"),
        ("KANNADA", "Kannada"),
        ("TAMIL", "Tamil"),
        ("TELUGU", "Telugu"),
        ("MALAYALAM", "Malayalam"),
    )

    name = models.CharField(max_length=50, unique=True, db_index=True)
    image = models.ImageField(null=True, blank=True, upload_to="media")
    language = models.CharField(max_length=10, choices=language_choices)
    is_active = models.BooleanField(default=True)

    class Meta(object):
        db_table = "movie"

    def __str__(self):
        return self.name


class Show(models.Model):
    # name = models.CharField(max_length=50, unique=True, db_index=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(
        Theatre, on_delete=models.CASCADE, null=True, blank=True
    )
    screen = models.IntegerField(default=1)
    timing = models.DateTimeField()
    duration = models.IntegerField(default=150)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta(object):
        db_table = "show"

    def __str__(self):
        return str(self.movie) + "|" + str(self.theatre) + "|" + str(self.timing)


class Seat(models.Model):
    number = models.CharField(max_length=3, null=True, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    class Meta(object):
        db_table = "seat"
        unique_together = ("number", "show")

    def __str__(self):
        return str(self.number) + "|" + str(self.show)
