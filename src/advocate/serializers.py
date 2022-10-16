from dataclasses import fields
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import (
    Advocate,
)

class AdvocateBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate


class SignupSerializer(AdvocateBaseSerializer):
    class Meta(AdvocateBaseSerializer.Meta):
        fields = [
            'id',
            'first_name', 
            'last_name',
            'username',
            'password',
            'email',
            'bio_short',
            'bio_long',
            'advocate_years_exp',
            'profile_pic',
            'company',
            'created',
            'updated',
        ]
        read_only_fields = ('id',)
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"write_only": True},
            "is_staff": {"write_only": True},
            "date_joined": {"write_only": True},
            "groups": {"write_only": True},
            "user_permissions": {"write_only": True},
            "last_login": {"write_only": True},
        }
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class AdvocateUpdateSerializer(AdvocateBaseSerializer):
    class Meta(AdvocateBaseSerializer.Meta):
        fields = [
            'id',
            'first_name', 
            'last_name',
            'email',
            'bio_short',
            'bio_long',
            'advocate_years_exp',
            'profile_pic',
            'company',
            'created',
            'updated',
        ]
        read_only_fields = ('id',)