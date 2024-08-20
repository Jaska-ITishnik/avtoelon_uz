from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices, Model, ForeignKey, CASCADE, CharField

from apps.models.managers import CustomUserManager


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        USER = 'user', 'User'
    username = None
    email = None
    first_name = None
    last_name = None
    phone_number = CharField(max_length=25, unique=True)
    type = CharField(max_length=20, choices=Type.choices, default=Type.USER)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'


class PhoneNumber(Model):
    user = ForeignKey('apps.User', CASCADE)
    phone = CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'phone'

