from django.urls import path

from github.api.views import getUsersRepos,get_AllExistingUsers


urlpatterns =[
path("repos/", getUsersRepos, name="users-list"),
path("allusers/",get_AllExistingUsers,name ="users-data")
]