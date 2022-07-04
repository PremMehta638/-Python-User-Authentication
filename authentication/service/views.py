from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def user_register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        confirm_password = request.POST.get('confirm_password')  
        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print('User register successfully. Please login with the same username and password')
            return redirect('login')
        else:
            print('Password and confirm password did not match')

    return render(request, 'service/register.html')


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Login Successfull')
            return redirect('profile')
        else:
            print('Invalid user name and password')
    return render(request, 'service/login.html')


@login_required()
def profile(request):
    return render(request, 'service/profile.html')