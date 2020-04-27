# Generated by Django 2.2.12 on 2020-04-15 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="movie", name="directed_by",),
        migrations.AddField(
            model_name="movie",
            name="directed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="directors",
                to="movies.Person",
            ),
        ),
    ]