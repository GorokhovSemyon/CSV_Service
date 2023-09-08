from rest_framework import serializers
from main.models import CustomUser

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'password')

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ('first_name', 'last_name', 'email', 'password')
