import pytest

from apps.models import Category


@pytest.fixture
def category():
    return Category.objects.create(name='Elektronika')