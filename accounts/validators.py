from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate(password):
    if not any(char.isdigit() for char in password):
        raise ValidationError(
            _("The password must contain at least one digit."),
            code='password_no_number',
        )
    if not any(char.islower() for char in password):
        raise ValidationError(
            _("The password must contain at least one lowercase letter."),
            code='password_no_lowercase',
        )
    if not any(char.isupper() for char in password):
        raise ValidationError(
            _("The password must contain at least one uppercase letter."),
            code='password_no_uppercase',
        )
