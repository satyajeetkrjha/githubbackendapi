from django.db import models

# Create your models here.
class GithubUser(models.Model):
    username = models.CharField(max_length=300,unique=True)
    total_followers = models.IntegerField()
    bio = models.TextField()
    total_publicrepos = models.IntegerField()
    name = models.TextField()
    location = models.CharField(max_length=500,blank=True)
    
    def __str__(self):
        return self.name
    
class Repository(models.Model):
    owner = models.ForeignKey(GithubUser,
                               on_delete=models.CASCADE,
                               related_name="repos")
    name = models.CharField(max_length=1000)

    
    
    
    