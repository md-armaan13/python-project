from django.urls import path
from . import views # . means current directory
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/',views.register,name='user-register'),#name is used to refer to this path
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='user-login'),#name is used to refer to this path
    #Here we are using the class based view for login these are the views provided by django for login and logout beccuse they implement the functionality of login and logout
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='user-logout'),
    path('profile/',views.profile,name='user-profile'),
] 
