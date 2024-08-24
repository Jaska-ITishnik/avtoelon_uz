from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, GenericAPIView, \
    ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.filters import AdvFilterSet
from apps.models import PhoneNumber, Adv, Category
from apps.models.news import News
from apps.models.users import User
from apps.pagination import CustomPageNumberPagination
from apps.serializers import AddPhoneSerializer, NewsSerializer, AdvModelSerializer, LoginModelSerializer, \
    CategoryModelSerializer, LogoutUserSerializer
from apps.serializers import SendVerificationCodeSerialize, VerifyCodeSerializer


class AdvListCreateAPIView(ListCreateAPIView):
    queryset = Adv.objects.all()
    serializer_class = AdvModelSerializer
    filterset_class = AdvFilterSet
    pagination_class = CustomPageNumberPagination


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class NewsListApiView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['many'] = True
        kwargs['fields'] = ('title', 'photo', 'created_at')
        return super().get_serializer(*args, **kwargs)

    def get_object(self):
        news = super().get_object()
        news.views_count += 1
        news.save()
        return news


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema(tags=['auth'])
class LoginGenericAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginModelSerializer
    permission_classes = AllowAny,

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=['auth'])
class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['auth'])
class SendVerificationCodeCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SendVerificationCodeSerialize
    permission_classes = AllowAny,


@extend_schema(tags=['auth'])
class VerifyCodeCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = VerifyCodeSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['auth'])
class PhoneNumberDestroyAPIView(DestroyAPIView):
    queryset = PhoneNumber.objects.all()

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)
        phones = PhoneNumber.objects.filter(user=self.request.user).order_by('created_at').values_list('phone',
                                                                                                       flat=True)
        deleted_phone = \
            PhoneNumber.objects.filter(id=self.request.parser_context.get('kwargs').get('pk')).values_list('phone',
                                                                                                           flat=True)[0]
        main_phone = User.objects.filter(id=self.request.user.id).values_list('phone_number', flat=True)[0]
        if qs.count() > 1 and (deleted_phone == main_phone):
            User.objects.filter(id=self.request.user.pk).update(phone_number=phones[1])

        if qs.count() > 1:
            return qs
        raise ValidationError("""To remove this phone number, first add another one.""")


@extend_schema(tags=['auth'])
class AddPhoneNumberCreateAPIView(CreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = AddPhoneSerializer


class AmountUserGenericAPIView(GenericAPIView):
    def get(self, request):
        user_amount = User.objects.count()
        return Response({"user_amount": user_amount}, status=status.HTTP_200_OK)
