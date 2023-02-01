from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from github.models import GithubUser
import requests
from urllib.error import HTTPError
import json
from github.api.serializers import UserSerializer

def validInvalidUsers(nonExistingUsers):
    invalidUserNames=[]
    for username in nonExistingUsers:
        url = f"https://api.github.com/users/{username}"
        res =requests.get(url)
        if res.status_code == 404:
            invalidUserNames.append(username)
        else:
            resjson = res.json()
            transformedData = dict()
            transformedData['name'] = resjson.get('name')
            transformedData['username'] = username
            transformedData['bio'] = "User has no bio" if resjson.get('bio', "") is None else resjson.get('bio', "")
            transformedData['total_followers']= resjson.get('followers')
            transformedData['total_publicrepos'] = resjson.get('public_repos')
            transformedData['location'] = "User has no location" if resjson.get('location', "") is None else resjson.get('location', "")
            serializer = UserSerializer(data=transformedData)
            if serializer.is_valid():
                serializer.save()
            print(res.json())
    return invalidUserNames

def get_nonexistingUers(usersTofetch):
    existingUers =[]
    nonexistingusers=[]
    for item in usersTofetch:
        user = GithubUser.objects.filter(username =item)
        if not user:
            nonexistingusers.append(item)
        else:
            existingUers.append(item)
    return nonexistingusers,existingUers

def get_users_list():
    userNames = []
    for i in range (1,10):
        userNames.append('username'+str(i))
    return userNames

def get_users_tofetch(request,userNames):
    userToFetch=[]
    print("inside ",userNames)
    for item in userNames:
        if request.query_params.get(item):
            userToFetch.append((request.query_params.get(item)))

    return userToFetch

@api_view(["GET", "POST"])
def getUserInfo(request,*args,**kwargs):
    userNames = get_users_list()
    usersToFetch = get_users_tofetch(request,userNames)
    nonExistingUsers,existingUsers = get_nonexistingUers(usersToFetch)
    invalidUsers =validInvalidUsers(nonExistingUsers)
    print(invalidUsers)
    return []

