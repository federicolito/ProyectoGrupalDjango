# Generated by Django 2.2 on 2020-12-04 04:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0020_factura_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo_comida',
            name='cant_bebida',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='combo_comida',
            name='cant_comida',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
