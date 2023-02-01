from django.db import models

# Create your models here.
class GithubUser(models.Model):
    username = models.CharField(max_length=100,unique=True)
    total_followers = models.PositiveIntegerField()
    bio = models.CharField(max_length=500)
    total_publicrepos = models.PositiveIntegerField()
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Repository(models.Model):
    owner = models.ForeignKey(GithubUser,
                               on_delete=models.CASCADE,
                               related_name="repos")
    name = models.CharField(max_length=1000)

    
    
    
    