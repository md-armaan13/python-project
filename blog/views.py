from typing import Optional
from django.forms.models import BaseModelForm
from django.shortcuts import render

from django.http import HttpResponse  # sending the response
from .models import Post
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

#class- views
from django.views.generic import (ListView, DetailView ,
 CreateView , UpdateView , DeleteView)

def home(request):
    posts = Post.objects.all()
    user = User.objects.filter(username='Armaan').first()
    context = {
        'posts': posts
    }
    # the Path for templates would be blog/templateName
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/model_viewtype.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    #template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model : Post
    fields = ['title','content']
    template_name = 'blog/post_form.html'
    #success_url = '/blog/home/'
    queryset = Post.objects.all()
    #what is queryset
    #queryset is used to get the list of objects from the database
    def form_valid(self,form):#`form_valid` method is called when valid form data has been POSTed.
        #`form` is a valid form instance.
        #`form_valid` should return an `HttpResponse
        #`form.instance` is the model instance that the form holds
        form.instance.author = self.request.user#setting the author of the post to the current user
        #`super` class is used to access the methods of the parent class
        #`super` is used to call the `form_valid` method of the parent class
        #here the parent class is `CreateView`
        return super().form_valid(form)

#<app>/model_viewtype.html

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model : Post
    fields = ['title','content']
    queryset = Post.objects.all()
    #template_name = 'blog/post_form.html'
    def test_func(self, *args, **kwargs) :
        post = self.get_object()
        if self.request.user == post.author:    
            return True
        return False
        
        

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model : Post
    success_url = '/blog/home/'
    template_name = 'blog/post_delete.html'
    queryset = Post.objects.all()
    def test_func(self, *args, **kwargs) :
        post = self.get_object()
        if self.request.user == post.author:    
            return True
        return False

def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
    