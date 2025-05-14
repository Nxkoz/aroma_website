from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 3:
            raise ValidationError(_("Пароль должен быть не короче 3 символов."))
        if password == '111':
            raise ValidationError(_("Пароль '111' запрещен."))

    def get_help_text(self):
        return _("Пароль должен быть не короче 3 символов и не равен '111'.")
