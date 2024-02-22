from django.http import JsonResponse
from .utils import get_all_movies, search_movies

def all_movies(request):
    movies = get_all_movies()
    return JsonResponse(movies)

def search(request):
    query = request.GET.get('query', '')
    results = search_movies(query)
    return JsonResponse(results)
