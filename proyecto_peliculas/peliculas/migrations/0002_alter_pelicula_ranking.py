# Generated by Django 4.2 on 2023-05-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='ranking',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
    ]
