from random import randrange

from django.contrib.auth import authenticate
from django.core.cache import cache
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.fields import CharField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.models import News, User, PhoneNumber, Adv, Category


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name'


class AdvModelSerializer(ModelSerializer):
    class Meta:
        model = Adv
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        super(NewsSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            not_allowed = set(exclude)
            for field_name in not_allowed:
                self.fields.pop(field_name)


class LoginModelSerializer(ModelSerializer):
    phone_number = CharField(max_length=50, write_only=True)
    password = CharField(max_length=50, write_only=True)
    access_token = CharField(max_length=255, read_only=True)
    refresh_token = CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = 'phone_number', 'access_token', 'refresh_token', 'password'

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, phone_number=phone_number, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials try again')
        user_tokens = user.tokens()

        return {
            'access_token': str(user_tokens.get('access_token')),
            'refresh_token': str(user_tokens.get('refresh_token')),
        }


class LogoutUserSerializer(Serializer):
    refresh_token = CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs.get('refresh_token')

        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            return self.fail('bad_token')


class AddPhoneSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    phone = CharField(max_length=20)

    class Meta:
        model = PhoneNumber
        fields = 'phone', 'user'

    def validate_phone(self, value):
        value = f"998{value}"
        phone_number = value
        if User.objects.filter(phone_number=value).exists() or PhoneNumber.objects.filter(phone=value).exists():
            raise ValidationError("""
                This phone number is already linked to another account.
            """)
        verification_code = randrange(1000, 9999)
        cache.set(phone_number, verification_code, timeout=1200)
        print(f"Your verification code: {verification_code}")
        return value


class SendVerificationCodeSerialize(Serializer):
    user = HiddenField(default=CurrentUserDefault())
    phone_number = CharField(max_length=20)

    def validate_phone_number(self, value):
        if f"998{value}" in User.objects.values_list('phone_number', flat=True):
            raise ValidationError(
                """This number is linked to another account. To add it to the current one, log in using this number and delete it from your account."""
            )
        if not value.isdigit() or len(value) > 9:
            raise ValidationError("Enter a valid phone number")
        return value

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        verification_code = randrange(1000, 9999)
        cache.set(phone_number, verification_code, timeout=1200)
        raise ValidationError(f'Your verification code: {verification_code}')


class VerifyCodeSerializer(Serializer):
    user = HiddenField(default=CurrentUserDefault())
    phone_number = CharField(max_length=20)
    code = CharField(max_length=4)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        code = attrs.get('code')
        cache_code = cache.get(phone_number)

        if cache_code is None:
            raise ValidationError('Validation code has been expired or invalid')
        if str(cache_code) != str(code):
            raise ValidationError('Validation code is not correct')
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        phone_number = f"998{validated_data['phone_number']}"
        user_instance, created = User.objects.get_or_create(phone_number=phone_number)

        if created:
            user_instance.user = user
            user_instance.save()

        User.objects.get_or_create(phone_number=phone_number)
        PhoneNumber.objects.get_or_create(phone=phone_number, user_id=user_instance.pk)
        cache.delete(phone_number)
        raise ValidationError("Registered successfully")
