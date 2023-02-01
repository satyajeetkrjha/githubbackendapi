from django.urls import path

from github.api.views import getUserInfo


urlpatterns =[
path("users/", getUserInfo, name="users-list"),
]