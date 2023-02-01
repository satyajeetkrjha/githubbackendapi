
from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from github.models import GithubUser
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    total_followers = serializers.IntegerField()
    bio = serializers.CharField()
    total_publicrepos = serializers.IntegerField()
    name = serializers.CharField()
    location = serializers.CharField()

    def create(self, data):
        return GithubUser.objects.create(**data)

