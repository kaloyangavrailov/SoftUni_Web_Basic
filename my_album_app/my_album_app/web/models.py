from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def check_letters_numbers_underscore(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError('"Ensure this value contains only letters, numbers, and underscore."')


# Create your models here.
class Profile(models.Model):
    USERNAME_MIN_LEN_VALIDATOR = 2
    USERNAME_MAX_LEN_VALIDATOR = 30

    username = models.CharField(
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(USERNAME_MIN_LEN_VALIDATOR), check_letters_numbers_underscore),
        max_length=USERNAME_MAX_LEN_VALIDATOR
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_NAME_MAX_LEN = 30
    GENRE_MAX_LEN = 30

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    R_AND_B_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSIC_CHOICES = (
        (POP_MUSIC,POP_MUSIC),
        (JAZZ_MUSIC,JAZZ_MUSIC),
        (R_AND_B_MUSIC,R_AND_B_MUSIC),
        (ROCK_MUSIC,ROCK_MUSIC),
        (COUNTRY_MUSIC,COUNTRY_MUSIC),
        (DANCE_MUSIC,DANCE_MUSIC),
        (HIP_HOP_MUSIC,HIP_HOP_MUSIC),
        (OTHER_MUSIC,OTHER_MUSIC)
    )

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=ALBUM_NAME_MAX_LEN
    )

    artist_name = models.CharField(
        null=False,
        blank=False,
        max_length=ALBUM_NAME_MAX_LEN
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=GENRE_MAX_LEN,
        choices=MUSIC_CHOICES
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(validators.MinValueValidator(0.0),)
    )
