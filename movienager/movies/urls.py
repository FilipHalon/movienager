from django.urls import include, path, re_path

import movies.views as views

movie_urls = [
    path("", views.MoviesView.as_view(), name="movies"),
    path("add", views.MovieAddView.as_view(), name="movie-add"),
    re_path(r"^edit/(?P<pk>\d+)$", views.MovieEditView.as_view(), name="movie-edit"),
    re_path(r"^delete/(?P<pk>\d+)$", views.MovieDeleteView.as_view(), name="movie-delete"),
]

person_urls = [
    path("", views.PeopleView.as_view(), name="people"),
    path("add", views.PersonAddView.as_view(), name="person-add"),
    re_path(r"^edit/(?P<pk>\d+)$", views.PersonEditView.as_view(), name="person-edit"),
    re_path(r"^delete/(?P<pk>\d+)$", views.PersonDeleteView.as_view(), name="person-delete"),
    re_path(r"^(?P<pk>\d+)$", views.PersonView.as_view(), name="person"),
]

urlpatterns = [
    path("movies/", include(movie_urls)),
    path("people/", include(person_urls)),
]
