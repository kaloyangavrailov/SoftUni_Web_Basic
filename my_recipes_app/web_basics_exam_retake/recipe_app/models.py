from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def check_two_chars_min(value):
    if len(value) < 2:
        raise ValidationError("Nickname must be at least 2 chars long!")


def check_starts_with_capital(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")


# Create your models here.
class Profile(models.Model):
    NICKNAME_MAX_LEN = 20
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    nickname = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=NICKNAME_MAX_LEN,
        validators=(check_two_chars_min,)
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=FIRST_NAME_MAX_LEN,
        validators=(check_starts_with_capital,)
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=LAST_NAME_MAX_LEN,
        validators=(check_starts_with_capital,)
    )

    chef = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    bio = models.TextField(
        null=True,
        blank=True
    )


class Recipe(models.Model):
    TITLE_MAX_LEN = 100
    TITLE_MIN_LEN = 10
    CUISINE_TYPE_MAX_LEN = 7
    FRENCH = 'French'
    CHINESE = 'Chinese'
    ITALIAN = 'Italian'
    BALKAN = 'Balkan'
    OTHER = 'Other'
    CUISINE_CHOICES = ((FRENCH, FRENCH),
                       (CHINESE, CHINESE),
                       (ITALIAN, ITALIAN),
                       (BALKAN, BALKAN),
                       (OTHER, OTHER)
                       )
    COOKING_TIME_MIN_VAL = 1
    COOKING_TIME_HELP_TEXT = "Provide the cooking time in minutes."
    INGREDIENTS_HELP_TEXT = "Ingredients must be separated by a comma and space."
    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=TITLE_MAX_LEN,
        validators=(validators.MinLengthValidator(TITLE_MIN_LEN),)
    )

    cuisine_type = models.CharField(
        null=False,
        blank=False,
        max_length=CUISINE_TYPE_MAX_LEN,
        choices=CUISINE_CHOICES
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text=INGREDIENTS_HELP_TEXT
    )

    instructions = models.TextField(
        null=False,
        blank=False
    )

    cooking_time = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text=COOKING_TIME_HELP_TEXT,
        validators=(validators.MinValueValidator(COOKING_TIME_MIN_VAL),)
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

