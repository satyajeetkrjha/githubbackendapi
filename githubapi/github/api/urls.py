from django.urls import path

from github.api.views import getUserInfo,get_AllExistingUsers


urlpatterns =[
path("users/", getUserInfo, name="users-list"),
path("allusers/",get_AllExistingUsers,name ="users-data")
]