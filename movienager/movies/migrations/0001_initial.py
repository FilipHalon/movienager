# Generated by Django 2.2.12 on 2020-04-15 13:39

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, upload_to=movies.models.person_photo_directory_path
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("prod_year", models.IntegerField()),
                (
                    "poster",
                    models.ImageField(upload_to=movies.models.poster_directory_path),
                ),
                ("short_desc", models.CharField(max_length=512)),
                (
                    "directed_by",
                    models.ManyToManyField(
                        related_name="directors", to="movies.Person"
                    ),
                ),
                (
                    "starring",
                    models.ManyToManyField(related_name="actors", to="movies.Person"),
                ),
            ],
        ),
    ]