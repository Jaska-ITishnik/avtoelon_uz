from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.models.news import News
from apps.serializers import NewsSerializer, NewsProductSerializer


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