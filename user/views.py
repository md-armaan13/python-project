from django.shortcuts import render , redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm , ProfileUpdateForm

def register(request):
    # here we using save function foe getting the form and 
    #submission of form when the request is a get request, it will return a blank form
    #when we submit the form the request is post and exeucte the if block
    if request.method == 'POST':#if the request is a post request
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        form = UserCreationForm(request.POST)#request.POST is used to get the data from the form
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('user-login')
    else :
        form = UserCreationForm()
    
    return render(request,'user/register.html',{'form':form})
    

@login_required
def profile(request):

    if request.method == 'POST':
        u_from = UserUpdateForm(request.POST,instance=request.user)#request.POST is used to get the data from the form
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)#request.FILES is used to get the image data
        #request.POST is used to get the data from the form
        if u_from.is_valid() and p_form.is_valid():
            u_from.save()
            p_form.save()
            messages.success(request,f'Account updated!')
            return redirect('user-profile')
    else :
        u_from = UserUpdateForm(instance=request.user)#instance is used to populate the form with the current user data
        p_form = ProfileUpdateForm(instance = request.user.profile)#instance is used to populate the form with the current user data

    context = {
        'u_form':u_from,
        'p_form':p_form
    }
    return render(request,'user/profile.html',context)

