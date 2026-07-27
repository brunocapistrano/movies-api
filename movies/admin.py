from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'actors', 'resume')
    search_fields = ('title', 'genre', 'actors')