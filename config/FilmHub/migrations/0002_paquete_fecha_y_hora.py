# Generated by Django 2.2 on 2020-11-18 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='fecha_y_hora',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
