from django.http import HttpResponse
from django.shortcuts import render


data = {
    'movies': [
        {
            'id': 1,
            'title': 'The Godfather',
            'year': '1972'
        },
        {
            'id': 2,
            'title': 'The Godfather: Part II',
            'year': '1974'
        },
        {
            'id': 3,
            'title': 'The Dark Knight',
            'year': '2008'
        }
    ]
}
def movies(request):
    # return HttpResponse("Hello, world. You're at the movies index.")
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Hello, world. You're at the movies index.")