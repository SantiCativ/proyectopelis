# Generated by Django 4.2 on 2023-06-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0007_alter_actor_foto_alter_director_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='foto',
            field=models.ImageField(upload_to='static/images/actor'),
        ),
        migrations.AlterField(
            model_name='director',
            name='foto',
            field=models.ImageField(upload_to='static/images/director'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='foto',
            field=models.ImageField(upload_to='static/images/pelicula'),
        ),
    ]