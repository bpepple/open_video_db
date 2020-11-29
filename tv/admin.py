from django.contrib import admin

from tv.models import Country, Episode, Genre, Language, Network, Season, Series


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    fields = ("name", "country", "website")


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    exclude = ("created_on", "modified")


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    fields = ("series", "number")


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    exclude = ("created_on", "modified")

