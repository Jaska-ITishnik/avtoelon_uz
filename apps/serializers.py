from random import randrange

from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import News, User, PhoneNumber


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name'


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(instance.user).data
        return data


class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = 'title', 'photo', 'created_at'

    # def get_primary_image(self, obj):
    #     first_image = obj.newsimage_set.first()
    #     if first_image:
    #         return NewsImageSerializer(first_image).data
    #     return None


class AddPhoneSerializer(ModelSerializer):
    phone = CharField(max_length=20)

    class Meta:
        model = PhoneNumber
        fields = 'phone',

    def validate_phone(self, value):
        value = f"998{value}"
        phone_number = value
        if User.objects.filter(phone_number=value).exists() or PhoneNumber.objects.filter(phone=value).exists():
            raise ValidationError("""
                This phone number is already linked to another account.
            """)
        verification_code = randrange(1000, 9999)
        cache.set(phone_number, verification_code, timeout=120)
        print(f"Your verification code: {verification_code}")
        return value


class SendVerificationCodeSerialize(Serializer):
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
        cache.set(phone_number, verification_code, timeout=120)
        raise ValidationError(f'Your verification code: {verification_code}')


class VerifyCodeSerializer(Serializer):
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
        phone_number = f"998{validated_data['phone_number']}"
        User.objects.get_or_create(phone_number=phone_number)
        cache.delete(phone_number)
        raise ValidationError("Registered successfully")
