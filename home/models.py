from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    post = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Friend(models.Model):
    users = models.ManyToManyField(User)


