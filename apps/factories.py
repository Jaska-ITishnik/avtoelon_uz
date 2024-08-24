from datetime import tzinfo

from django.utils import timezone
from factory.django import DjangoModelFactory
import factory
from apps.models import User


class UserDjangoModelFactory(DjangoModelFactory):
    data_joined = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    phone_number = factory.Faker()
    class Meta:
        model = User