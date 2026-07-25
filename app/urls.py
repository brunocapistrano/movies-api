from django.contrib import admin
from django.urls import path

from genres.views import genre_view, genre_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_view, name='genre'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail'),
]
