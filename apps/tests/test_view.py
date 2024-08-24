import pytest
from rest_framework.reverse import reverse_lazy


@pytest.mark.django_db
class TestView:
    def test_category(self, client, category):
        url = reverse_lazy('category-list')
        response = client.get(url)
        data = response.json()
        assert data[0]['id'] == category.id