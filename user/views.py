from django.shortcuts import render , redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
            return redirect('blog-home')
    else :
        form = UserCreationForm()
    
    return render(request,'user/register.html',{'form':form})
    


def login(request):
    return render(request,'user/login.html')

