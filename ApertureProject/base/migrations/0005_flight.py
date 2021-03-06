# Generated by Django 4.0.3 on 2022-05-06 02:35

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_airplane_on_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('Source_City', django_countries.fields.CountryField(max_length=2)),
                ('Destination_City', django_countries.fields.CountryField(max_length=2)),
                ('Flight_type', models.CharField(max_length=30)),
                ('Flight_Duration', models.DurationField()),
                ('Boarding_Time', models.CharField(max_length=30)),
            ],
        ),
    ]
