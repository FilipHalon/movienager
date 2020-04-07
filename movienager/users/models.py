from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        blank=True,
        null = True,
        help_text=_('30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=20, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), primary_key=True)
    photo = models.ImageField(blank=True)

    objects = ""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
