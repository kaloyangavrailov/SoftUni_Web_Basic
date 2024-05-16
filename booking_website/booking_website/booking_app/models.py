from django.core import validators
from django.db import models
from booking_website.booking_app import custom_validators


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 45
    LAST_NAME_MIST_LEN = 2
    USERNAME_MIN_LEN = 5
    USERNAME_MAX_LEN = 30

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length= FIRST_NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
                    custom_validators.check_first_letter_capital,
                    custom_validators.check_if_chars_only_letters
                    ),

    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=LAST_NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(LAST_NAME_MIST_LEN),
                    custom_validators.check_first_letter_capital,
                    custom_validators.check_if_chars_only_letters,
                    )
    )

    username = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=USERNAME_MAX_LEN,
        validators=(validators.MinLengthValidator(USERNAME_MIN_LEN),
                    custom_validators.check_alpha_numerical_special_chars,
                    custom_validators.check_alpha_numerical_special_chars,)
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    profile_picture_url = models.URLField(
        null=True,
        blank=True,
    )


class Apartment(models.Model):
    NAME_MIN_LEN = 5
    NAME_MAX_LEN = 30
    BIG_BED_MAX_NUMBER = 2
    BIG_BED_MIN_NUMBER = 2
    SMALL_BED_MAX_NUMBER = 2
    SMALL_BED_MIN_NUMBER = 2
    ADDRESS_MAX_LEN = 100

    name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(NAME_MIN_LEN),
                    custom_validators.check_if_chars_only_letters,)
    )

    address = models.CharField(
        null=False,
        blank=False,
        max_length=ADDRESS_MAX_LEN
    )

    booked = models.BooleanField(
        null=True,
        blank=True,
        default=False
    )

    number_big_bed = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(validators.MaxLengthValidator(BIG_BED_MAX_NUMBER),
                    validators.MinLengthValidator(BIG_BED_MIN_NUMBER),)
    )

    additional_beds = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(validators.MaxLengthValidator(SMALL_BED_MAX_NUMBER),
                    validators.MinLengthValidator(SMALL_BED_MIN_NUMBER),)
    )

