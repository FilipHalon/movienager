from django.urls import path, re_path

import movies.views as views

urlpatterns = [
    path("movies", views.MoviesView.as_view(), name="movies"),
    path("movies/add", views.MovieAddView.as_view(), name="movie-add"),
    re_path(r"^movies/edit/(?P<pk>\d+$)", views.MovieEditView.as_view(), name="movie-edit"),
    re_path(r"^movies/delete/(?P<pk>\d+$)", views.MovieDeleteView.as_view(), name="movie-delete"),
    path("people", views.PeopleView.as_view(), name="people"),
]
