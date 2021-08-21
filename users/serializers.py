from rest_framework import serializers
from django.contrib.auth.models import User

# General User Serializer 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User()
        user.set_password(validated_data['password'])
        validated_data['password'] = user.password
        return super().create(validated_data)


# Serializer for Groups' user
class GroupUserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ('id', 'username', 'email', 'password', 'groups')
        extra_kwargs = {
            'password': {'write_only': True},
        }