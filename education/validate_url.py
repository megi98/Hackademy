from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validator(url):
    try:
        validate = URLValidator()
        validate(url)
    except (ValueError, ValidationError):
        raise ValidationError('Not a valid URL')
