from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import (
    AddPhoneNumberCreateAPIView,
    AdvListCreateAPIView,
    AmountUserGenericAPIView,
    CategoryListCreateAPIView,
    LoginGenericAPIView,
    LogoutAPIView,
    NewsDetailAPIView,
    NewsListApiView,
    PhoneNumberDestroyAPIView,
    SendVerificationCodeCreateAPIView,
    UserListAPIView,
    VerifyCodeCreateAPIView, CategoryDocumentViewSet,
)

router = DefaultRouter()

router.register('categofghjries', CategoryDocumentViewSet, 'categories')

urlpatterns = [

    path('users/', UserListAPIView.as_view(), name='users'),
    path('', include(router.urls)),
    path('adv-list/', AdvListCreateAPIView.as_view(), name='adv-list'),
    path('category-list/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('news/', NewsListApiView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('user-amount/', AmountUserGenericAPIView.as_view(), name='col-user'),
    path('login/', LoginGenericAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('auth/register-send-code/', SendVerificationCodeCreateAPIView.as_view(), name='send-code'),
    path('auth/register-verify-code/', VerifyCodeCreateAPIView.as_view(), name='verify-code'),
    path('auth/delete-phone/<int:pk>/', PhoneNumberDestroyAPIView.as_view(), name='delete-phone'),
    path('auth/add-phone/', AddPhoneNumberCreateAPIView.as_view(), name='add-phone')
]