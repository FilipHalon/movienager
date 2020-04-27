# Generated by Django 2.2.12 on 2020-04-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20200421_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(related_name='actor', through='movies.Cast', to='movies.Person', verbose_name='Starring'),
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='Name', max_length=128, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='Surname', max_length=128, verbose_name='Last name'),
            preserve_default=False,
        ),
    ]