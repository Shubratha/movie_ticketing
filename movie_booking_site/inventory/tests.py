from django.db.backends.sqlite3.base import IntegrityError
from django.test import TestCase

from .models import *


class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        City.objects.create(name="Mumbai")

    def test_name_max_length(self):
        city = City.objects.get(id=1)
        max_length = city._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


class TheatreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        city = City.objects.create(name="Mumbai")
        Theatre.objects.create(name="PVR", fk_city=city, total_screens=1)

    def test_duplicate_object_creation(self):
        city = City.objects.get(id=1)
        theatre = Theatre(name="PVR", fk_city=city, total_screens=1)
        with self.assertRaises(Exception) as raised:
            theatre.save()
        self.assertEqual(IntegrityError, type(raised.exception))

    def test_name_max_length(self):
        theatre = Theatre.objects.get(id=1)
        max_length = theatre._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Movie.objects.create(name="TesTMovie", language="English")

    def test_valid_language_entered(self):
        movie = Movie.objects.create(name="Language Check", language="Kannada")
        self.assertEqual(movie.language, "Kannada")

    def test_name_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)
