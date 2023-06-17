from django import forms
from django.contrib.auth.models import User
from .models import Profile



class UserUpdateForm(forms.ModelForm):
    #why we are using this form is because we want to update the username and ema
    username = forms.CharField()
    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    #we are taking the image variable from forms ImageField beacuse we want to update the image
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']