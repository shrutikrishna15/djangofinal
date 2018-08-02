

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Post(models.Model):

    post = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.post


class Friend(models.Model):
    users = models.ManyToManyField(User)




class Comment(models.Model):
    post = models.ForeignKey('home.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
