# Generated by Django 4.0.3 on 2022-03-14 16:38

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('simetra_app', '0003_alter_city_options_city_latitude_city_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationOfCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
            ],
        ),
    ]