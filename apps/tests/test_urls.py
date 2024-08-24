import pytest
from django.urls import reverse_lazy
from rest_framework import status


@pytest.mark.django_db
class TestUrl:
    def test_news_detail(self, client):
        url = reverse_lazy('news-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert '/api/v1/news' == url

    def test_adv_list(self, client):
        url = reverse_lazy('adv-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert '/api/v1/adv-list' == url
