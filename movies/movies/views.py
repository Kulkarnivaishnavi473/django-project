from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseRedirect

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html',{'movies': data})
def homePage(request):
    return HttpResponse("Hello, this is the home page!")
def details(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/details.html', {'movies': data})

def addMovie(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/add.html')

def deleteMovie(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("Movie does not exist")
    movie.delete()
    return HttpResponseRedirect('/movies')