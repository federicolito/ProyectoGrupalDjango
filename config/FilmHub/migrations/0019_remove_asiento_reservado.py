# Generated by Django 2.2 on 2020-12-04 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0018_auto_20201204_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asiento',
            name='reservado',
        ),
    ]
