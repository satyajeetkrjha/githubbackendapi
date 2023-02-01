from django.contrib import admin

# Register your models here.
from github.models import GithubUser
admin.site.register(GithubUser)