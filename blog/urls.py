from django.urls import path
from . import views # . means current directory


urlpatterns = [
   path('',views.home,name='blog-home'),#name is used to refer to this path
]
