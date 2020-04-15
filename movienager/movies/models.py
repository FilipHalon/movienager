from django.db import models

def person_photo_directory_path(instance, filename):
    return f"people/{instance.id}/photos/{filename}"

def poster_directory_path(instance, filename):
    return f"movies/{instance.id}/posters/{filename}"


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(blank=True, upload_to=person_photo_directory_path)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    prod_year = models.IntegerField()
    poster = models.ImageField(upload_to=poster_directory_path)
    short_desc = models.CharField(max_length=512)
    starring = models.ManyToManyField(Person, related_name="actors")
    directed_by = models.ManyToManyField(Person, related_name="directors")

    def __str__(self):
        return self.title
