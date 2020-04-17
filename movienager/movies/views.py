from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import edit

from movies.models import Movie, Person


# Create your views here.
class MovieMixin:
    model = Movie
    context_object_name = "movies"
    fields = "__all__"
    success_url = "/movies"


class MoviesView(MovieMixin, generic.ListView):
    template_name = "movie/movies.html"


class MovieAddView(MovieMixin, edit.CreateView):
    template_name = "movie/forms/movie-add.html"


class MovieEditView(MovieMixin, generic.UpdateView):
    template_name = "movie/forms/movie-edit.html"


class MovieDeleteView(MovieMixin, generic.DeleteView):
    template_name = "movie/forms/movie-delete.html"


class PersonMixin:
    model = Person
    context_object_name = "people"
    fields = "__all__"
    success_url = "/people"


class PeopleView(PersonMixin, generic.ListView):
    template_name = "person/people.html"


class PersonAddView(PersonMixin, edit.CreateView):
    template_name = "person/forms/person-add.html"


class PersonEditView(PersonMixin, generic.UpdateView):
    template_name = "person/forms/person-edit.html"


class PersonDeleteView(PersonMixin, generic.DeleteView):
    template_name = "person/forms/person-delete.html"


class PersonView(generic.DetailView):
    model = Person
    template_name = "person/person.html"
