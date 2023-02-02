from django.contrib import admin

# Register your models here.
from github.models import GithubUser,Repository
admin.site.register(GithubUser)
admin.site.register(Repository)
