from django.db.models.signals import post_save , pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#import os
#from django.conf import settings   
import os

#import settings module
from django.conf import settings

#this is a decorator which takes the signal as argument
@receiver(post_save,sender=User)#when a user is saved then send this signal
#this function is called when the signal is recieved
# when the user is saved then the signal is sent and the reciever is the create_profile function
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance,image='default.jpg')
    

@receiver(pre_save, sender=Profile)
def delete_old_profile_picture(sender, instance, **kwargs):
    if instance.pk:#if the instance is already created
        print("instance.pk")
        try:
            old_instance = sender.objects.get(pk=instance.pk)#get the old instance
            print(old_instance)
            if old_instance.image != instance.image:
                # Delete the old profile picture
                if old_instance.image:
                    old_picture_path = old_instance.image.path
                    path = os.path.join(settings.MEDIA_ROOT, str(old_picture_path))
                    print(path)
                    if os.path.exists(path):
                     os.remove(path)
        except sender.DoesNotExist:
            pass