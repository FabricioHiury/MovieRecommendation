from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.all_movies, name='all_movies'),
    path('search/', views.search, name='search'),
]
