from django.db.models import CharField
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, GenericAPIView, DestroyAPIView
from rest_framework.response import Response

from apps.models.news import News
from apps.models.user import User
from apps.serializers import NewsSerializer
from apps.serializers import SendVerificationCodeSerialize, VerifyCodeSerializer
from apps.models import PhoneNumber
from apps.serializers import AddPhoneSerializer
from apps.serializers import NewsDetailSerializer


class NewsListCreateApiView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_object(self):
        news = super().get_object()
        news.views_count += 1
        news.save()
        return news


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


@extend_schema(tags=['auth'])
class SendVerificationCodeCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SendVerificationCodeSerialize


@extend_schema(tags=['auth'])
class VerifyCodeCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = VerifyCodeSerializer


@extend_schema(tags=['auth'])
class DeletePhoneNumberDestroyAPIView(DestroyAPIView):
    queryset = PhoneNumber.objects.all()

    def get_queryset(self):
        user = self.request.user
        return PhoneNumber.objects.filter(user=user)

    def delete(self, request, *args, **kwargs):
        p_number_list = PhoneNumber.objects.filter(user=self.request.user).values_list()
        if not p_number_list:
            raise ValidationError(
                """To remove this phone number, first add another one."""
            )
        return self.destroy(request, *args, **kwargs)


@extend_schema(tags=['auth'])
class AddPhoneNumberCreateAPIView(CreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = AddPhoneSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AmountUserGenericAPIView(GenericAPIView):
    def get(self, request):
        user_amount = User.objects.count()
        return Response({"user_amount": user_amount}, status=status.HTTP_200_OK)