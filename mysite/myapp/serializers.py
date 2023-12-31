from rest_framework import serializers
from .models import App, Sdk, AppSdk
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token


# Create your serializers here.
class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model =App
        fields = ['id', 'name', 'company_url', 'genre_id', 'release_date', 'artwork_large_url', 'seller_name', 'five_star_ratings', 'four_star_ratings', 'three_star_ratings', 'two_star_ratings', 'one_star_ratings']


class SdkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sdk
        fields = ['id', 'name', 'slug', 'url', 'description']


class AppSdkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSdk
        fields = ['id', 'app_id', 'sdk_id', 'installed']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#
#         extra_kwargs = {
#             'password':{
#                 'write_only': True,
#                 'required': True
#             }
#         }
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user