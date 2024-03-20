from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.all_movies, name='all_movies'),
    path('search/', views.search, name='search'),
    path('movies/<int:movie_id>/', views.movie_details_by_id, name='movie-details-by-id'),
]
