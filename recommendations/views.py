from django.http import JsonResponse
from .utils import get_all_movies, search_movies, search_movie_by_id

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