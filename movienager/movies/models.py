from django.db import models


def person_photo_directory_path(instance, filename):
    return f"people/{instance.id}/photos/{filename}"


def poster_directory_path(instance, filename):
    return f"movies/{instance.id}/posters/{filename}"


# Create your models here.
class Person(models.Model):
    photo = models.ImageField(blank=True, upload_to=person_photo_directory_path, verbose_name="Photo")
    name = models.CharField(max_length=128, verbose_name="Name")

    def __str__(self):
        return self.name


class Movie(models.Model):
    poster = models.ImageField(upload_to=poster_directory_path, verbose_name="Poster")
    title = models.CharField(max_length=128, verbose_name="Title")
    prod_year = models.IntegerField(verbose_name="Production year")
    short_desc = models.CharField(max_length=512, verbose_name="Short description")
    starring = models.ManyToManyField(Person, related_name="actors", verbose_name="Starring")
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
