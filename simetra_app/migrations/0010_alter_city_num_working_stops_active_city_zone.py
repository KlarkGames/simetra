# Generated by Django 4.0.3 on 2022-04-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simetra_app', '0009_remove_city_bool_day_tariff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='num_working_stops_active_city_zone',
            field=models.IntegerField(default=0, verbose_name='Количество остановочных пунктов в черте активной зоны города'),
        ),
    ]
