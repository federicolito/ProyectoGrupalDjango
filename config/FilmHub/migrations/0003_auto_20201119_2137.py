# Generated by Django 2.2 on 2020-11-19 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0002_asiento_elegido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asiento',
            name='elegido',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='asientos',
        ),
        migrations.AddField(
            model_name='asiento',
            name='sala',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Sala'),
        ),
    ]