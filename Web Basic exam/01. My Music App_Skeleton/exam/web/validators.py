from django.core.exceptions import ValidationError


def validate_only_letters_numbers_underscore(value):
    for letter in value:
        if not (letter.isalpha() or letter.isdigit() or letter == '_'):
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


def validation_positive_float_price(value):
    if value < 0:
        raise ValidationError('The price can not be negative')
