import requests
from django.conf import settings

def get_all_movies():
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
    }
    response = requests.get(url, params=params)
    return response.json()

def search_movies(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'query': query,
        'language': 'en-US',
    }
    response = requests.get(url, params=params)
    return response.json()
