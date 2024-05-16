from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def check_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 25
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 35
    LAST_NAME_MIN_LEN = 1
    EMAIL_MAX_LEN = 40
    PASSWORD_MAX_LEN = 20
    PASSWORD_MIN_LEN = 8
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=FIRST_NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(FIRST_NAME_MIN_LEN), check_starts_with_letter,)
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=LAST_NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(LAST_NAME_MIN_LEN), check_starts_with_letter,)
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
        max_length=EMAIL_MAX_LEN
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=PASSWORD_MAX_LEN,
        validators=(validators.MinLengthValidator(PASSWORD_MIN_LEN),),
        help_text='*Password length requirements: 8 to 20 characters'
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18
    )


def check_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Fruit name should contain only letters!")


class Fruit(models.Model):
    FRUIT_NAME_MAX_LEN = 30
    FRUIT_NAME_MIN_LEN = 2

    name = models.CharField(
        null=False,
        blank=False,
        max_length=FRUIT_NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(FRUIT_NAME_MIN_LEN), check_only_letters,),
        unique=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_constraint_name',
                                    violation_error_message='"This fruit name is already in use! Try a new one."')
        ]