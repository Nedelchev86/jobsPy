from django.core.exceptions import ValidationError


def validate_phone_number(value):

    if not value.isdigit():
        raise ValidationError('Phone number must contain only numbers.')


def validate_start_with_upper(value):
    if not value[0].isupper():
        raise ValidationError('Name must start with an uppercase letter.')

