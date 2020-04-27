from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .managers import AdjustedUserManager


# Create your models here.
class User(AbstractUser):
    REGULAR_USER = 1
    ADMIN = 2
    TYPES = ((REGULAR_USER, "Regular user"), (ADMIN, "Admin"))

    username = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
        help_text=("30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[UnicodeUsernameValidator()],
        error_messages={"unique": ("A user with that username already exists."),},
    )
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(primary_key=True)
    photo = models.ImageField(blank=True, upload_to="profile_photos")
    user_type = models.PositiveSmallIntegerField(choices=TYPES, default=REGULAR_USER)

    objects = AdjustedUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_permission()

    def set_permission(self):
        if self.user_type == self.ADMIN:
            self.add_permission(self)
        else:
            self.remove_permission(self)

    @classmethod
    def get_permission(cls, user, perm_codename):
        content_type = ContentType.objects.get_for_model(cls)
        return Permission.objects.get(
            codename=perm_codename, content_type=content_type
        )

    def add_permission(self, user):
        permission = self.get_permission(self, "add_user")
        user.user_permissions.add(permission)

    def remove_permission(self, user):
        permission = self.get_permission(self, "add_user")
        user.user_permissions.remove(permission)
