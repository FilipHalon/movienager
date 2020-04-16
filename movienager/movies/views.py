from django.shortcuts import render
from django.views import generic

from movies.models import Movie


# Create your views here.
class MoviesView(generic.ListView):
    model = Movie
    template_name = "movie/movies.html"
    context_object_name = "movies"