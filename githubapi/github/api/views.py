from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from github.models import GithubUser

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
    nonexistingusers,existingusers = get_nonexistingUers(usersToFetch)
    print(nonexistingusers)
    print(existingusers)

    pass

