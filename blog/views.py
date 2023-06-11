from django.shortcuts import render

from django.http import HttpResponse # sending the response

posts = [
    {
        'author' : 'CoreyMS',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'August 28, 2018'
    }
]


def home (request) :
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context) #the Path for templates would be blog/templateName

def about (request) :
    return render(request,'blog/about.html')
# Create your views here.
