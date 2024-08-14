from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices, Model, ForeignKey, CASCADE, CharField


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        USER = 'user', 'User'

    type = CharField(max_length=20, choices=Type.choices, default=Type.USER)

    class Meta:
        db_table = 'user'


class PhoneNumber(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE)
    phone = CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'phone'
