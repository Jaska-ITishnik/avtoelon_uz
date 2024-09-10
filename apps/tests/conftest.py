import pytest
from apps.factories import UserFactory
from apps.models import Category


@pytest.fixture
def category():
    return Category.objects.create(name='Elektronika')

@pytest.fixture
def users():
    UserFactory.create_batch(20)
