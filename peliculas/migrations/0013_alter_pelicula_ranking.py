# Generated by Django 4.2 on 2023-07-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0012_critica_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='ranking',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=2, null=True),
        ),
    ]
