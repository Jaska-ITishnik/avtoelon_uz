from django.urls import path

from apps.views import NewsListCreateApiView, SendVerificationCodeCreateAPIView, \
    VerifyCodeCreateAPIView
from apps.views import AmountUserGenericAPIView
from apps.views import DeletePhoneNumberDestroyAPIView
from apps.views import AddPhoneNumberCreateAPIView
from apps.views import NewsDetailAPIView

urlpatterns = [
    path('news', NewsListCreateApiView.as_view(), name='news-list'),
    path('news-products/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('user-amount', AmountUserGenericAPIView.as_view(), name='col-user'),
    path('auth/register-send-code', SendVerificationCodeCreateAPIView.as_view(), name='send-code'),
    path('auth/register-verify-code', VerifyCodeCreateAPIView.as_view(), name='verify-code'),
    path('auth/delete-phone/<int:pk>', DeletePhoneNumberDestroyAPIView.as_view(), name='delete-phone'),
    path('auth/add-phone/', AddPhoneNumberCreateAPIView.as_view(), name='add-phone')
]