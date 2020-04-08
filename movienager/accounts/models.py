from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
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
    photo = models.ImageField(blank=True, upload_to='profile_photos/')
    user_type = models.PositiveSmallIntegerField(choices=TYPES, default=REGULAR_USER)

    objects = AdjustedUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = (
            ("manage", "Can get access to the list of users, and add, edit and delete them")
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.user_type == self.ADMIN:
            self.grant_permission(self)

    @classmethod
    def grant_permission(cls, user, codename="manage"):
        content_type = ContentType.objects.get_for_model(cls)
        permission = Permission.objects.get(
            codename=codename,
            content_type=content_type
        )
        user.user_permission.add(permission)
