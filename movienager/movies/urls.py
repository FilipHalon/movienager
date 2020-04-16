from django.urls import path, re_path

import movies.views as views

urlpatterns = [
    path("movies", views.MoviesView.as_view(), name="movies"),
    path("movies/add", views.MovieAddView.as_view(), name="movie-add"),
    re_path(r"^movies/(?P<pk>\d+$)", views.MovieEditView.as_view(), name="movie-edit"),
]
