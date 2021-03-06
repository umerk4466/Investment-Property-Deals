# Generated by Django 3.1.6 on 2021-03-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deals', '0003_auto_20210303_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='UkPostcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(blank=True, max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=255)),
                ('longitude', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UkTownAndCounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town_and_county', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='PlacesUk',
        ),
    ]
