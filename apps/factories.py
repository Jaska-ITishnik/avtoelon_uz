import random

import factory
from apps.models import User
from django.utils import timezone
from factory.django import DjangoModelFactory

codes = ['90', '91', '93', '94', '97', '88', '33']


class UserFactory(DjangoModelFactory):
    date_joined = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    # phone_number = factory.LazyAttribute(lambda o: f"998{o.phone_}")
    type = factory.Iterator(list(zip(*User.Type.choices))[0])

    class Meta:
        model = User

    class Params:
        phone_ = factory.Faker('msisdn')

    @factory.lazy_attribute
    def phone_number(self):
        return f"998{random.choice(codes)}{self.phone_[:7]}"

class CategorFactory(DjangoModelFactory):
    pass