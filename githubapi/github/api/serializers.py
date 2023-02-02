
from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from github.models import GithubUser,Repository
# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField()
#     total_followers = serializers.IntegerField()
#     bio = serializers.CharField()
#     total_publicrepos = serializers.IntegerField()
#     name = serializers.CharField()
#     location = serializers.CharField()
#
#     def create(self, data):
#         return GithubUser.objects.create(**data)
#
# class RepoSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     owner = serializers.StringRelatedField(read_only=True)
#
#     def create(self,data):
#         return Repository.objects.create(**data)


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    #repos = RepoSerializer(many=True,read_only=True)
    class Meta:
        model = GithubUser
        fields = '__all__'





