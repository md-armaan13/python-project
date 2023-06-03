from django.shortcuts import render

from django.http import HttpResponse # sending the response


def home (request) :
    return HttpResponse('<h1>Blog Home</h1>')


# Create your views here.
