from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html', locals())

def forgot_password(request):
    return render(request, 'forgot-password.html', locals())

def register(request):
    return render(request, 'register.html', locals())