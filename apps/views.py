from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from apps.models.news import News
from apps.serializers import NewsSerializer, NewsProductSerializer
from models import User
from serializers import SendVerificationCodeSerialize, VerifyCodeSerializer


class NewsListCreateApiView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = AllowAny,

    def get_object(self):
        news = super().get_object()
        news.views_count += 1
        news.save()
        return news


class NewsProductAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsProductSerializer
    lookup_field = 'pk'

class SendVerificationCodeCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SendVerificationCodeSerialize
    permission_classes = AllowAny,

class VerifyCodeCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = VerifyCodeSerializer
    permission_classes = AllowAny,