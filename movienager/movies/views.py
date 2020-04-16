from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import edit

from movies.models import Movie


# Create your views here.
class MoviesView(generic.ListView):
    model = Movie
    template_name = "movie/movies.html"
    context_object_name = "movies"


class MovieAddView(edit.CreateView):
    model = Movie
    fields = "__all__"
    success_url = "/movies"
    template_name = "movie/forms/movie-add.html"