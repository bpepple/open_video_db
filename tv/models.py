import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import CustomUser


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Language(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ["name"]


class Network(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    website = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


def current_year():
    return datetime.date.today().year


def max_value_next_year(value):
    next_year = current_year() + 1
    return MaxValueValidator(next_year)(value)


class Series(models.Model):
    CONTINUING = "CO"
    ENDED = "EN"
    UPCOMING = "UP"
    STATUS_CHOICES = [
        (CONTINUING, "Continuing"),
        (ENDED, "Ended"),
        (UPCOMING, "Upcoming"),
    ]

    name = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField(
        default=current_year(),
        validators=[MinValueValidator(1935), max_value_next_year],
    )
    overview = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=CONTINUING)
    genre = models.ManyToManyField(Genre, blank=True)
    website = models.URLField(blank=True)
    imdb = models.URLField(blank=True)
    tvdb = models.URLField(blank=True)
    tmdb = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(CustomUser, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self) -> str:
        return f"{self.name} ({self.year})"

    class Meta:
        verbose_name_plural = "Series"
        ordering = ["name"]


class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.series.name} Season {self.number}"

    class Meta:
        unique_together = ["series", "number"]
        ordering = ["series__name", "number"]


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    air_date = models.DateField()
    runtime = models.PositiveSmallIntegerField(blank=True)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    is_movie = models.BooleanField(default=False)
    is_finale = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        CustomUser, related_name="creator", default=1, on_delete=models.SET_DEFAULT
    )
    edited_by = models.ForeignKey(
        CustomUser, related_name="editor", default=1, on_delete=models.SET_DEFAULT
    )

    def __str__(self) -> str:
        return self.name

