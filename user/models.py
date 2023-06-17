from django.db import models
from django.contrib.auth.models import User

from PIL import Image
# Create your models here.
#this is a one to one relationship with the user model
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)#if the user is deleted then the profile is also deleted
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')#upload_to is the directory where the image is stored
    #we have to install pillow for this
    def __str__(self):
        return f'{self.user.username} Profile'
    

    def save (self):
        
        super().save()#this will run the save method of the parent class
        #beacuse we want to resize the image before saving it

        img = Image.open(self.image.path)#this will open the image that we have uploaded
        if img.height > 300 or img.width > 300:
            max_size = (300,300)
            img.thumbnail(max_size)#this will resize the image
            img.save(self.image.path)#this will save the image