from django.core.exceptions import ValidationError


def check_first_letter_capital(value):
    if not value[0].isupper():
        raise ValidationError('First letter needs to be capital!')


def check_if_chars_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Please use only letters!')


def check_alpha_numerical_special_chars(value):
    for ch in value:
        if not ch.isalnum() or ch not in '!_':
            raise ValidationError('Please use only letters and numbers as well as "!" and "_"!')

