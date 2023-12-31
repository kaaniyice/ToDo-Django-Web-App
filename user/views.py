from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')
        password2 = request.POST.get('user_password_again')
        # Ensure username and password are not empty
        if not username or not password:
            # Handle empty fields
            return render(request, 'register.html', {'error': 'Please fill in all fields.'})

        # Check for existing user
        if User.objects.filter(username=username).exists():
            # Handle username already exists
            return render(request, 'register.html', {'error': 'Username already exists.'})

        # If want to have email change None to email and get the value via email = request.POST.get('user_email')
        if password == password2:
            try:
                user = User.objects.create_user(username, None, password)
                return HttpResponseRedirect(reverse("user:login"))
            except Exception as error:
                # Handle registration errors
                return render(request, 'register.html', {'error': str(error)})
        else:
            return render(request, 'register.html', {'error': "Passwords don't match"})

    else:
        # Render the registration form
        return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Attempt authentication
        user = authenticate(request, username=username, password=password)
        if not username or not password:
            # Handle empty fields
            return render(request, 'login.html', {'error': 'Please fill in all fields.'})
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            # Invalid credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        # Render the login form
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("user:login"))
