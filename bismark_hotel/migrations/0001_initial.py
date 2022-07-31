# Generated by Django 4.0.4 on 2022-07-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('room_type', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('number_of_guests', models.IntegerField()),
                ('number_of_rooms', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('room_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
