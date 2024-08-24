from django.urls import path

from apps.views import SendVerificationCodeCreateAPIView, \
    VerifyCodeCreateAPIView, NewsListApiView, AdvListCreateAPIView, LoginGenericAPIView, CategoryListCreateAPIView, \
    LogoutAPIView
from apps.views import AmountUserGenericAPIView
from apps.views import PhoneNumberDestroyAPIView
from apps.views import AddPhoneNumberCreateAPIView
from apps.views import NewsDetailAPIView

urlpatterns = [
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