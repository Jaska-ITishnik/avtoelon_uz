from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices, Model, ForeignKey, CASCADE, CharField, DateTimeField
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models.managers import CustomUserManager


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        USER = 'user', 'User'

    username = None
    email = None
    phone_number = CharField(max_length=25, unique=True)
    type = CharField(max_length=20, choices=Type.choices, default=Type.USER)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token)
        }


class PhoneNumber(Model):
    user = ForeignKey('apps.User', CASCADE)
    phone = CharField(max_length=20, unique=True)
    created_at = DateTimeField(auto_now_add=True)
