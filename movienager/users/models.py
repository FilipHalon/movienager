from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import AdjustedUserManager


# Create your models here.
class User(AbstractUser):
    REGULAR_USER = 1
    ADMIN = 2
    TYPES = (
        (REGULAR_USER, 'Regular user'),
        (ADMIN, 'Admin')
    )

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
    user_type = models.PositiveSmallIntegerField(choices=TYPES, default=REGULAR_USER)

    objects = AdjustedUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = (
            ("manage", "Can get access to the list of users, and add, edit and delete them")
        )