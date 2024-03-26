import requests
from django.conf import settings
import numpy as np

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

genre_mapping = get_genre_mapping()
movies = get_all_movies()['results']

unique_genre_names = sorted(set(genre_mapping[genre_id] for movie in movies for genre_id in movie['genre_ids'] if genre_id in genre_mapping))

all_genres_vectors = np.array([genres_vector(movie) for movie in movies])

def weighted_genres_vector(movie):
    vector = np.zeros(len(unique_genre_names))
    genre_ids = []
    
    if 'genres' in movie:
        genre_ids = [genre['id'] for genre in movie['genres']]
    elif 'genre_ids' in movie:
        genre_ids = movie['genre_ids']
    
    for index, genre_id in enumerate(genre_ids):
        if genre_id in genre_mapping:
            genre_name = genre_mapping[genre_id]
            genre_index = unique_genre_names.index(genre_name)
            weight = 2 if index == 0 else 1
            vector[genre_index] = weight
    return vector

target_movie = search_movie_by_id(movie_id)
target_movie_vector = weighted_genres_vector(target_movie)

def find_first_genre_index(genre_vector):
    first_genre_indices = np.where(genre_vector == 1)[0]
    if len(first_genre_indices) > 0:
        return first_genre_indices[0]
    return None

target_first_genre_index = find_first_genre_index(target_movie_vector)

def has_same_first_genre(target_genre_index, movie_vector):
    return movie_vector[target_genre_index] == 1

exact_matches_indices = [i for i, vector in enumerate(all_genres_vectors) if has_same_first_genre(target_first_genre_index, vector)]

for index in exact_matches_indices:
    print(movies[index]['title'])

def genres_vector(movie):
    vector = np.zeros(len(unique_genre_names))
    genre_ids = []
    if 'genres' in movie:
        genre_ids = [genre['id'] for genre in movie['genres']]
    elif 'genre_ids' in movie:
        genre_ids = movie['genre_ids']
    
    for genre_id in genre_ids:
        if genre_id in genre_mapping:
            genre_name = genre_mapping[genre_id]
            genre_index = unique_genre_names.index(genre_name)
            vector[genre_index] = 1
    return vector



def find_second_genre_index(genre_vector):
    genre_indices = np.where(genre_vector == 1)[0]
    if len(genre_indices) > 1:
        return genre_indices[1]  
    return None

target_second_genre_index = find_second_genre_index(target_movie_vector)
def has_same_genre(target_genre_index, movie_vector):
    if target_genre_index is None:
        return False 
    return movie_vector[target_genre_index] == 1

exact_matches_indices_limited = exact_matches_indices[:10]

for index in exact_matches_indices_limited:
    print(movies[index]['title'])


def get_genre_id_by_name(genre_name, genre_mapping):
    name_to_id_mapping = {name: id for id, name in genre_mapping.items()}
    return name_to_id_mapping.get(genre_name)

def find_target_second_genre_id(target_movie_vector, unique_genre_names, genre_mapping):
    second_genre_index = find_second_genre_index(target_movie_vector)
    if second_genre_index is not None:
        second_genre_name = unique_genre_names[second_genre_index]
        return get_genre_id_by_name(second_genre_name, genre_mapping)
    return None

target_second_genre_id = find_target_second_genre_id(target_movie_vector, unique_genre_names, genre_mapping)
