from rest_framework import serializers
from .models import Profile,Comment,Category,Sport
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True,'required':True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_name','profile_photo','profile_email','phone_number','created_at')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','image')

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'

