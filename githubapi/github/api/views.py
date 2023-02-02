from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from github.models import GithubUser,Repository
import requests
from urllib.error import HTTPError
import json
from github.api.serializers import UserSerializer,RepoSerializer


def validInvalidUsers(nonExistingUsers,existingUsers):
    invalidUserNames=[]
    createdUsers=[]
    for username in nonExistingUsers:
        url = f"https://api.github.com/users/{username}"
        res =requests.get(url)
        if res.status_code == 404:
            invalidUserNames.append(username)
        else:
            resjson = res.json()
            transformedData = dict()
            transformedData['name'] = "User has no Name" if resjson.get('name', "") is None else resjson.get('name', "")
            transformedData['username'] = username
            transformedData['bio'] = "User has no bio" if resjson.get('bio', "") is None else resjson.get('bio', "")
            transformedData['total_followers']= resjson.get('followers')
            transformedData['total_publicrepos'] = resjson.get('public_repos')
            transformedData['location'] = "User has no location" if resjson.get('location', "") is None else resjson.get('location', "")
            serializer = UserSerializer(data=transformedData)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data['id'])
                userCreated =dict()
                userCreated['id'] =serializer.data.get('id')
                userCreated['username']=username
                createdUsers.append(userCreated)

    #after creation make api call and save their repos and add all different data

    getRepos(createdUsers,existingUsers)

def getRepos(createdUsers,existingUers):

    print (createdUsers)

    for item in createdUsers:
        url = "https://api.github.com/users/{}".format(item.get('username')) + "/repos"
        token = "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"
        headers = {
            "authorization": "Bearer{}".format(token)
        }
        api_link = requests.get(url, headers=headers)
        api_data = api_link.json()
        repos_Data = (api_data)
        repos = []
        [repos.append(items['name']) for items in repos_Data]
        print("repos",repos)
        userId = item.get('id')
        repoData ={}
        for index,item in enumerate(repos):
            print(item)
            print(index)
            repoData['githubuser'] =userId
            repoData['name'] =repos[index]
            serializer = RepoSerializer(data = repoData)
            if serializer.is_valid():
                serializer.save()




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
    invalidUsers =validInvalidUsers(nonExistingUsers,existingUsers)
    print(invalidUsers)
    return []

