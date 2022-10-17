from dataclasses import fields
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import (
    Advocate,
    Link,
    Company,
    TechStack,    
)

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'logo', 'website', 'created', 'updated']
        read_only_fields = ('id', )


class TechStackSrializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'created', 'updated']
        read_only_fields = ('id', )


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


class LinkListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        links = [Link(**link) for link in validated_data]
        return Link.objects.bulk_create(links)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['name', 'advocate', 'followers', 'url', 'created', 'updated']
        read_only_fields = ('id',)
        list_serializer_class = LinkListSerializer


class LinkRequestChildSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    followers = serializers.IntegerField(required=False)
    url = serializers.URLField(required=True)


class LinkRequestBodySerializer(serializers.Serializer):
    links = serializers.ListField(child=LinkRequestChildSerializer(), required=True, allow_empty=False)


class AdvocateResponseSerializer(AdvocateBaseSerializer):
    company = CompanySerializer(read_only=True)
    tech_stack = TechStackSrializer(read_only=True, many=True)
    links = LinkSerializer(read_only=True, many=True)

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
            'tech_stack',
            'links',
            'created',
            'updated',
        ]
        read_only_fields = ('id',)