from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as loginuser,logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import  UserCreationForCusomize
from .decorators import  unauthenticated,allowed_users



@unauthenticated
def login(request):
 
    if request.method == "POST":
        username = request.POST.get('username');
        password = request.POST.get('password');
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('this is user',user)
            loginuser(request, user)
            return redirect('/tasks')
        else:
            messages.info(request, 'username or password are incorrect')
            return render(request,'auth/login.html',{})
            

    return render(request,'auth/login.html',{})

@unauthenticated
def register(request):

    form = UserCreationForCusomize()
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForCusomize(request.POST or None)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('username')
            group = Group.objects.get(name="users")
            user.groups.add(group)
            messages.success(request, 'user successefully registred for ' + name)
            return redirect('/account/login')
    context = {
        'form':form
    }
     
    return render(request,'auth/register.html',context)


def logoutuser(request):
    logout(request)
    return redirect('/account/login')