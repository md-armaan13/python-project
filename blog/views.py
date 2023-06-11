from django.shortcuts import render

from django.http import HttpResponse  # sending the response
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    # the Path for templates would be blog/templateName
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
