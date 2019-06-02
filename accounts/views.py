from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # User has filled the form and now press submit button
        if request.POST['password1'] == request.POST['password2']:
            # checking both pass matching
            try:
                # We declared a try block
                user = User.objects.get(username=request.POST['username'])
                # First we will try to get the user object
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
                # If we succeed in getting user object model than the User Already Exists
            except User.DoesNotExist:
                # If Error Ocuured in getting User Model than the User Doesn exists
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # So lets create a User model with Passing Values username & password
                auth.login(request,user)
                #This will login the user
                return redirect('home')
                # Redirect it to home page
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info (get method)
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            #user already exists with correct Login Info
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})
    else:

        # User is Requesting Login page (get method)
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')