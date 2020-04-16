from django.urls import path

import movies.views as views

urlpatterns = [
    path("movies", views.MoviesView.as_view(), name="movies"),
    path("movies/add", views.MovieAddView.as_view(), name="movie-add"),
]
