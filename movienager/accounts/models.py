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

    class Meta:
        permissions = (("manage user", "Can list, add, edit and delete users"),)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_permission()

    def set_permission(self):
        if self.user_type == self.ADMIN:
            self.change_permission(self)
        else:
            self.change_permission(self, method="revoke")

    @classmethod
    def change_permission(cls, user, perm_codename="manage user", method="grant"):
        content_type = ContentType.objects.get_for_model(cls)
        permission = Permission.objects.get(
            codename=perm_codename, content_type=content_type
        )
        if method == "grant":
            user.user_permissions.add(permission)
        elif method == "revoke":
            user.user_permissions.remove(permission)
