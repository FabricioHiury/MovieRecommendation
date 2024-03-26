from django.http import JsonResponse, HttpResponseBadRequest
from .utils import get_all_movies, search_movies, search_movie_by_id, get_genre_mapping
from django.views.decorators.http import require_http_methods
import json

#essa funcao traz todos os filmes
def all_movies(request):
    movies = get_all_movies()
    return JsonResponse(movies)

#essa funcao faz uma busca do filme pelo titulo
def search(request):
    query = request.GET.get('query', '')
    results = search_movies(query)
    return JsonResponse(results)

#essa funcao recebe um id e busca as informacoes sobre ele
def movie_details_by_id(request, movie_id):
    movie_details = search_movie_by_id(movie_id)
    if movie_details:
        return JsonResponse(movie_details)
    else:
        return JsonResponse({'error': 'Movie not found'}, status=404)
    
@require_http_methods(["POST"])
def similar_movies(request):
    try:
        body = json.loads(request.body)
        movie_id = body.get('movieId')
        if not movie_id:
            return JsonResponse({'error': 'MovieId não fornecido'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    target_movie = search_movie_by_id(movie_id)
    if not target_movie:
        return JsonResponse({'error': 'Filme não encontrado'}, status=404)
    
    genre_mapping = get_genre_mapping()
    target_genres = target_movie.get('genres', [])
    target_genre_ids = {genre['id'] for genre in target_genres}

    all_movies = get_all_movies().get('results', [])
    similar_movies = []
    for movie in all_movies:
        if movie['id'] != int(movie_id) and set(genre['id'] for genre in movie.get('genres', [])) & target_genre_ids:
            movie_genres = [genre_mapping[genre_id] for genre_id in movie.get('genre_ids', []) if genre_id in genre_mapping]
            similar_movies.append({'title': movie['title'], 'genres': movie_genres})
        if len(similar_movies) == 10:
            break  

    return JsonResponse({'similar_movies': similar_movies})