from django.db import models


def person_photo_directory_path(instance, filename):
    return f"people/{instance.name}/photos/{filename}"


def poster_directory_path(instance, filename):
    return f"movies/{instance.title}/posters/{filename}"


# Create your models here.
class Person(models.Model):
    photo = models.ImageField(blank=True, upload_to=person_photo_directory_path, verbose_name="Photo")
    first_name = models.CharField(max_length=128, verbose_name="First name")
    last_name = models.CharField(max_length=128, verbose_name="Last name")

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name


class Movie(models.Model):
    poster = models.ImageField(upload_to=poster_directory_path, verbose_name="Poster")
    title = models.CharField(max_length=128, verbose_name="Title")
    prod_year = models.IntegerField(verbose_name="Production year")
    short_desc = models.CharField(max_length=512, verbose_name="Short description")
    starring = models.ManyToManyField(Person, through="Cast", related_name="actor", verbose_name="Starring")
    directed_by = models.ForeignKey(
        Person,
        blank=True,
        null=True,
        related_name="director",
        on_delete=models.SET_NULL,
        verbose_name="Directed by"
    )

    def __str__(self):
        return self.title


class Cast(models.Model):
    movie = models.ForeignKey(Movie, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Movie")
    actor = models.ForeignKey(Person, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Actor")
    role = models.CharField(max_length=128)
