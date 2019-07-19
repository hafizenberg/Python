from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'loginapp/index.html',{})

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"successfull")
            return redirect('index')
        else:
            messages.success(request,"Fuck you!!")
            return redirect('login_user')
    else:
        return render(request,'loginapp/login.html',{})
