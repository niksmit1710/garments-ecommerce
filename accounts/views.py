from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )
        login(request, user)
        return redirect('orders:checkout')

    return render(request, 'accounts/signup.html')
