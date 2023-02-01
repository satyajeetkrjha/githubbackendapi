from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

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
            userToFetch.append((item))

    return userToFetch

@api_view(["GET", "POST"])
def getUserInfo(request,*args,**kwargs):
    print(request.query_params.get('username'))
    userNames = get_users_list()
    print("userNames ",userNames)
    usersToFetch = get_users_tofetch(request,userNames)
    print(usersToFetch)

    pass

