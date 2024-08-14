from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView

from apps.views import NewsListCreateApiView

urlpatterns = [
    path('news', NewsListCreateApiView.as_view(), name='news-list'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
# comment!!!