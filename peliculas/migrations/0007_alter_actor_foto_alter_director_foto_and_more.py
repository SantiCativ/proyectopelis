# Generated by Django 4.2 on 2023-06-19 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0006_alter_pelicula_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='foto',
            field=models.ImageField(upload_to='peliculas/static/images/actor'),
        ),
        migrations.AlterField(
            model_name='director',
            name='foto',
            field=models.ImageField(upload_to='peliculas/static/images/director'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='foto',
            field=models.ImageField(upload_to='peliculas/static/images/pelicula'),
        ),
    ]