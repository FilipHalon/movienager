from django.contrib import admin

from movies.models import Movie, Person


# Register your models here.
admin.site.register(Movie)
admin.site.register(Person)
