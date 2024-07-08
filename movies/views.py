from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie


def movies(request):
    # return HttpResponse("Hello, world. You're at the movies index.")
    data = {'movies': Movie.objects.all()}
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Hello, world. You're at the movies index.")

def detail(request, movie_id):
    data = Movie.objects.get(id=movie_id)
    print("The data: ", data)
    return render(request, 'movies/detail.html', {'movie': data})


def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/add.html')


def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if not movie:    # if movie doesn't exist
        raise Http404("Movie does not exist")
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        if title and year:
            movie.title = title
        if year:
            movie.year = year
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/edit.html', {'movie': movie})


def delete(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")

    movie.delete()
    return HttpResponseRedirect('/movies')


