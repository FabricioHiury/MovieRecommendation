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

def search_movie_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
    }
    response = requests.get(url, params=params)
    if response.ok:
        return response.json()
    else:
        return None
    
def get_genre_mapping():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "en-US"
    }
    response = requests.get(url, params=params)
    genres = response.json().get('genres', [])
    return {genre['id']: genre['name'] for genre in genres}