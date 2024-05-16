# Generated by Django 4.2.11 on 2024-04-23 16:45

import booking_website.booking_app.custom_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(5), booking_website.booking_app.custom_validators.check_if_chars_only_letters])),
                ('address', models.CharField(max_length=100)),
                ('booked', models.BooleanField(blank=True, default=False, null=True)),
                ('number_big_bed', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.MinLengthValidator(2)])),
                ('additional_beds', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.MinLengthValidator(2)])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), booking_website.booking_app.custom_validators.check_first_letter_capital, booking_website.booking_app.custom_validators.check_if_chars_only_letters])),
                ('last_name', models.CharField(max_length=45, validators=[django.core.validators.MinLengthValidator(2), booking_website.booking_app.custom_validators.check_first_letter_capital, booking_website.booking_app.custom_validators.check_if_chars_only_letters])),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(5), booking_website.booking_app.custom_validators.check_alpha_numerical_special_chars, booking_website.booking_app.custom_validators.check_alpha_numerical_special_chars])),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
