# Generated by Django 3.1.6 on 2021-04-05 18:42

import Deals.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deals', '0002_auto_20210405_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='image',
            field=models.ImageField(upload_to=Deals.models.get_image_filename),
        ),
    ]