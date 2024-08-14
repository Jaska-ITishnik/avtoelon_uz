from random import randrange

from django.core.cache import cache
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import News, User, PhoneNumber
from apps.models.news import NewsImage


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


class NewsProductSerializer(serializers.ModelSerializer):
    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = '__all__'

    def get_primary_image(self, obj):
        first_image = obj.newsimage_set.first()
        if first_image:
            return NewsImageSerializer(first_image).data
        return None


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = 'photo',


class PhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = 'id', 'phone', 'user'

    def validate_phone(self, value):
        user_id = self.instance.id if self.instance else None
        if User.objects.filter(phone=value).exclude(id=user_id).exists():
            raise serializers.ValidationError('Phone number is already registered')

    def validate(self, data):
        user = data['user'] if 'user' in data else self.instance.user
        if self.instance and user.phonenumber_set.count() == 1:
            if self.instance.phone == data.get('phone', self.instance.phone):
                raise serializers.ValidationError('Before delete this you must add another one!')
        return data


class SendVerificationCodeSerialize(Serializer):
    phone = CharField(max_length=20)

    def validate_phone(self, value):
        if not value.isdigit() or len(value) > 9:
            raise ValidationError("Enter a valid phone number")
        return value

    def create(self, validated_data):
        phone = validated_data['phone']
        verification_code = randrange(1000, 9999)

        cache.set(phone, verification_code, timeout=120)

        raise ValidationError(f'Your verification code: {verification_code}')


class VerifyCodeSerializer(Serializer):
    phone = CharField(max_length=20)
    code = CharField(max_length=4)

    def validate(self, attrs):
        phone = attrs.get('phone')
        code = attrs.get('code')
        cache_code = cache.get(phone)

        if cache_code is None:
            raise ValidationError('Validation code has been expired or invalid')
        if str(cache_code) != str(code):
            raise ValidationError('Validation code is not correct')
        return attrs

    def create(self, validated_data):
        phone = validated_data['phone']
        cache.delete(phone)
        raise ValidationError('Validation code is correct')
