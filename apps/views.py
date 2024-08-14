from rest_framework.generics import ListCreateAPIView

from apps.models import News
from apps.serializers import NewsSerializer


class NewsListCreateApiView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_object(self):
        news = super().get_object()
        news.views += 1
        news.save()
        return news
