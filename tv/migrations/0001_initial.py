# Generated by Django 3.1.3 on 2020-11-29 22:40

import django.core.validators
import django.db.models.deletion
import tv.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={"verbose_name_plural": "Countries", "ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="Series",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "year",
                    models.PositiveSmallIntegerField(
                        default=2020,
                        validators=[
                            django.core.validators.MinValueValidator(1935),
                            tv.models.max_value_next_year,
                        ],
                    ),
                ),
                ("overview", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CO", "Continuing"),
                            ("EN", "Ended"),
                            ("UP", "Upcoming"),
                        ],
                        default="CO",
                        max_length=2,
                    ),
                ),
                ("website", models.URLField(blank=True)),
                ("imdb", models.URLField(blank=True)),
                ("tvdb", models.URLField(blank=True)),
                ("tmdb", models.URLField(blank=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tv.country"
                    ),
                ),
                (
                    "edited_by",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("genre", models.ManyToManyField(blank=True, to="tv.Genre")),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tv.language"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Series", "ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="Season",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.PositiveSmallIntegerField()),
                (
                    "series",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tv.series"
                    ),
                ),
            ],
            options={
                "ordering": ["series__name", "number"],
                "unique_together": {("series", "number")},
            },
        ),
        migrations.CreateModel(
            name="Network",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("website", models.URLField(blank=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tv.country"
                    ),
                ),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="Episode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.PositiveSmallIntegerField()),
                ("name", models.CharField(max_length=255)),
                ("overview", models.TextField(blank=True)),
                ("air_date", models.DateField()),
                ("runtime", models.PositiveSmallIntegerField(blank=True)),
                ("is_movie", models.BooleanField(default=False)),
                ("is_finale", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "edited_by",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="editor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "network",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tv.network"
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tv.season"
                    ),
                ),
            ],
        ),
    ]
