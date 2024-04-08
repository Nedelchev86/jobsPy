from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_deadline_after_today(value):
    today = timezone.now().date()
    if value <= today:
        raise ValidationError('Deadline must be after today.')