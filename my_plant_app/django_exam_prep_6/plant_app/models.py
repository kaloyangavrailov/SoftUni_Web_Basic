from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def first_letter_capital(value):
    if not value[0].isupper():
        raise ValidationError(f"Your name must start with a capital letter!")


def only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(f'Plant name should contain only letters!')


# Create your models here.
class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    username = models.CharField(
        null=False,
        blank=False,
        max_length=USERNAME_MAX_LEN,
        validators=(validators.MinLengthValidator(USERNAME_MIN_LEN),)
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=FIRST_NAME_MAX_LEN,
        validators=(first_letter_capital,)
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=LAST_NAME_MAX_LEN,
        validators=(first_letter_capital,)
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )


class Plant(models.Model):
    PLANT_TYPE_MAX_LEN = 14
    PLANT_NAME_MAX_LEN = 20
    PLANT_NAME_MIN_LEN = 2
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'
    PLANT_TYPE_CHOICES = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS)
    )

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=PLANT_TYPE_MAX_LEN,
        choices=PLANT_TYPE_CHOICES
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=PLANT_NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(PLANT_NAME_MIN_LEN), only_letters,),
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False
    )
