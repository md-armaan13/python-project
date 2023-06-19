from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse 


class Post(models.Model):
    # max length of the title is 100 characters
    title = models.CharField(max_length=100)
    content = models.TextField()  # no limit on the length of the text
    # auto_now = True means that the date will be updated automatically
    date_posted = models.DateTimeField(default=timezone.now)
    # when the post is updated
    # use auto_now_add = True if you want the date to be updated only when the post is created
    # default = timezone.now can also be used
    # if the user is deleted, the post will also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # if you want to keep the post even after the user is deleted, use on_delete = models.SET_NULL
    # this is one to many relationship, one user can have many posts, but one post can have only one user
    def __str__(self):
            return self.title
    
    #this method is used to redirect to the post detail page after creating a post
    #`get_absolute_url` method is used to redirect to a specific route after creating a post 
    def get_absolute_url(self):
            
         return reverse('post-detail',kwargs={'pk':self.pk})