import pytest
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.reverse import reverse_lazy


@pytest.mark.django_db
class TestView:
    def test_category(self, client, category):
        url = reverse_lazy('category-list')
        response = client.get(url)
        data = response.json()
        assert data[0]['id'] == category.id

    def test_users(self, client, users):
        url = reverse_lazy('users')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()
        assert len(response) == 4
        allowed_fields = {'last_name', 'id', 'is_active', 'password', 'date_joined', 'user_permissions', 'is_superuser',
                          'phone_number', 'last_login', 'groups', 'first_name', 'is_staff', 'type'}
        assert set(response['results'][0]) == allowed_fields
        next_page_url = f"{url}?{urlencode({"page": 2})}"
        assert next_page_url in response['next']

        response = client.options(url)
        http_methods = response.headers.get('Allow')
        http_methods = set(map(lambda x: x.lower(), http_methods.split(', ')))
        allowed_http_methods = {'post', 'get', 'head', 'options'}
        assert http_methods == allowed_http_methods
        response = client.get(next_page_url)
        assert response.status_code == status.HTTP_200_OK
