from django.urls import path
from . import views # . means current directory
from .views import PostListView , PostDetailView , PostCreateView , PostUpdateView

urlpatterns = [
   path('home/',PostListView.as_view(),name='blog-home'),#name is used to refer to this path
   path('about/',views.about,name='blog-about'),
   path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
   path('post/new/',PostCreateView.as_view(),name='post-create'),
   path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
   path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post-delete'),
   #pk is primary key of the post
   #<int > is used to specify that the pk is an integer
]
