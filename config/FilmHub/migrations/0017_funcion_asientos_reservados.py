# Generated by Django 2.2 on 2020-12-04 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0016_auto_20201203_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcion',
            name='asientos_reservados',
            field=models.ManyToManyField(blank=True, to='FilmHub.Asiento'),
        ),
    ]
