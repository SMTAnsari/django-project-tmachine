from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Feature
from video.models import Feature
from django.db.models import Q
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password1']
        if password == password2:
            if Feature.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            elif Feature.objects.filter(name=name).exists():
                messages.error(request, 'name already exists')
                return redirect('register')
            else:  
                User1 = Feature.objects.create(email=email, password=password, name=name)
                User1.save()
                print('Registration successful')
                return redirect('/Home')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']
        # Check if user exists in the Feature model
        try:
            features = Feature.objects.all()
            feature = Feature.objects.get(email=username_or_email)
        except Feature.DoesNotExist:
            feature = None

        if feature is not None and feature.password == password:
            # Authentication successful
            return render(request, 'index.html', {'username': feature.name})
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def index(request):
    return render(request,"index.html")