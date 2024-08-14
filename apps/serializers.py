from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

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
        fields = ['photo']


class PhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = 'id', 'phone', 'user'

    # def validate_phone(self, value):
    #     user_id = self.instance.id if self.instance else None
    #     if User.objects.filter(phone=value).exclude(id=user_id).exists():
    #         raise serializers.ValidationError('Phone number is already registered')
    #
    # def validate(self, data):
    #     user = data['user'] if 'user' in data else self.instance.user
    #     if self.instance and user.phonenumber_set.count() == 1:
    #         if self.instance.phone == data.get('phone', self.instance.phone):
    #             raise serializers.ValidationError('Before delete this you must add another one!')
    #     return data
