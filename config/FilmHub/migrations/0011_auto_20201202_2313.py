# Generated by Django 2.2 on 2020-12-02 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FilmHub', '0010_factura_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='combo_comida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FilmHub.Combo_Comida'),
        ),
    ]
