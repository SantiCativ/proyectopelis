# Generated by Django 4.2 on 2023-05-26 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_alter_critica_peli'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='ranking',
        ),
    ]