from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import edit

from movies.models import Movie, Person


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


class MovieEditView(generic.UpdateView):
    model = Movie
    fields = "__all__"
    success_url = "/movies"
    template_name = "movie/forms/movie-edit.html"


class MovieDeleteView(generic.DeleteView):
    model = Movie
    success_url = "/movies"
    template_name = "movie/forms/movie-delete.html"


class PeopleView(generic.ListView):
    model = Person
    template_name = "person/people.html"
    context_object_name = "people"


class PersonAddView(edit.CreateView):
    model = Person
    fields = "__all__"
    success_url = "/people"
    template_name = "person/forms/person-add.html"


class PersonEditView(generic.UpdateView):
    model = Person
    fields = "__all__"
    success_url = "/people"
    template_name = "person/forms/person-edit.html"


class PersonDeleteView(generic.DeleteView):
    model = Person
    success_url = "/people"
    template_name = "person/forms/person-delete.html"


class PersonView(generic.DetailView):
    model = Person
    template_name = "person/person.html"
