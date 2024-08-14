from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView

from apps.views import NewsListCreateApiView, NewsProductAPIView
from views import SendVerificationCodeCreateAPIView, VerifyCodeCreateAPIView

urlpatterns = [
    path('api/v1/news', NewsListCreateApiView.as_view(), name='news-list'),
    path('api/v1/news-products/<int:pk>/', NewsProductAPIView.as_view(), name='news-detail'),
    path('api/v1/send-code', SendVerificationCodeCreateAPIView.as_view(), name='send-code'),
    path('api/v1/verify-code', VerifyCodeCreateAPIView.as_view(), name='verify-code'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
# comment!!!