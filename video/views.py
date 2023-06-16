from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Feature
from video.models import Feature
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
import random



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

            else:  
                

                # Send registration confirmation email
                a,otp=otpGenerate()
                subject = 'Registration Confirmation'
                message = render_to_string('Email_Template.html', {'name': name,'otp':otp})
                from_email = 'maheshreddyqq@gmail.com'  # Replace with your Gmail email address
                recipient_email = email
                mail_sent(subject,message,from_email,recipient_email,True)
                user = Feature.objects.create(email=email, password=password, name=name, otp = a)
                user.save()
                # email = EmailMultiAlternatives(
                #     subject=subject,
                #     body=message,
                #     from_email=from_email,
                #     to=[recipient_email]
                # )
                # email.attach_alternative(message, "text/html")
                # email.send()

                print('Registration successful')
                return redirect('otp', email=email)
                # return redirect(otp(email))
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

def otpGenerate():
    otp=random.randint(1000,9999)
    a=''
    for i in range(3):
        a+=str(otp)[int(i)]+'-'
    else:
        a+=str(otp)[-1]
    return otp,a
    
def mail_sent(subject,message,from_email,to_email,temp):
    if temp:
        email = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email=from_email,
        to=[to_email]
                )
        email.attach_alternative(message, "text/html")
        email.send()
    else:
        email(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[to_email]
        )
        email.send()
    return
    

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
    elif request.method == 'GET':
        return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def otp(request,email):
    print(email)
    context = {
        'email': email,
    }
    if request.method == 'POST':
        a=request.POST['digit-1']
        b=request.POST['digit-2']
        c=request.POST['digit-3']
        d=request.POST['digit-4']
        otp=int(str(a)+str(b)+str(c)+str(d))
        try:
            user = Feature.objects.get(email=email)
        except Feature.DoesNotExist:
            messages.error(request, 'Invalid email')
            return redirect('register')  # Redirect to the registration page or any other appropriate page
        
        # Check if the OTP matches
        if user.otp == otp:
            # OTP is valid, do something
            messages.success(request, 'OTP is valid')
            return redirect('/Home')  # Redirect to a success page or any other appropriate page
        else:
            # OTP is invalid
            messages.error(request, 'Invalid OTP')
            return redirect('otp', email=email)  # Redirect back to the OTP page with the email pre-filled
    

    return render(request, "OTP_Template.html", context)

def otpForgot(request,email):
    print(email)
    context = {
        'email': email,
    }
    if request.method == 'POST':
        a=request.POST['digit-1']
        b=request.POST['digit-2']
        c=request.POST['digit-3']
        d=request.POST['digit-4']
        otp=int(str(a)+str(b)+str(c)+str(d))
        try:
            user = Feature.objects.get(email=email)
        except Feature.DoesNotExist:
            messages.error(request, 'Invalid email')
            return redirect('login')  # Redirect to the registration page or any other appropriate page
        
        # Check if the OTP matches
        if user.otp == otp:
            # OTP is valid, do something
            messages.success(request, 'OTP is valid')
            return redirect('reset', email=email)  # Redirect to a success page or any other appropriate page
        else:
            # OTP is invalid
            messages.error(request, 'Invalid OTP')
            return redirect('otpForgot', email=email)  # Redirect back to the OTP page with the email pre-filled
    

    return render(request, "OTP_Template.html", context)

def forgot(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Feature.objects.filter(email=email).exists():
            feature = Feature.objects.get(email=email)
            name=feature.name
            a,otp=otpGenerate()
            subject = 'Registration Confirmation'
            message = render_to_string('Email_Template.html', {'name': name,'otp':otp})
            from_email = 'maheshreddyqq@gmail.com'  # Replace with your Gmail email address
            recipient_email = email
            mail_sent(subject,message,from_email,recipient_email,True)
            Feature.objects.filter(email=email).update(otp=a)
            return redirect('otpForgot', email=email)



    return render(request, "forgot email template.html")

def reset(request,email):
    print(email)
    context = {
        'email': email,
    }
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password1']
        print(password2,password)
        if password == password2:
            try:
                feature = Feature.objects.get(email=email)
                feature.password = password
                feature.save()
                return redirect('login')
            except Feature.DoesNotExist:
                messages.error(request, 'Invalid email')
                return redirect('reset', email=email)
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('reset', email=email)
    return render(request,"reset_password.html", context)