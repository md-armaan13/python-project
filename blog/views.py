from django.shortcuts import render

from django.http import HttpResponse  # sending the response
from .models import Post
from django.contrib.auth.models import User



def home(request):
    posts = Post.objects.all()
    user = User.objects.filter(username='Armaan').first()
    print(user.profile.image.url)
    print(posts[0].author.profile.image.url)
    context = {
        'posts': posts
    }
    # the Path for templates would be blog/templateName
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
