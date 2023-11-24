from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
def home(request):
    return render(request,"home.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name already used")
                return redirect('/register/')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('/login/')
        else:
            messages.info(request,"password not match")
            return redirect('/register/')
        return redirect('/')
    return render(request, "register.html")
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/loginsuccess/')
        else:
            messages.info(request,"Invalid User")
            return redirect('/login/')
    return render(request,"login.html")
def loginsuccess(request):
    return render(request,"loginsuccess.html")
def form(request):
    return render(request,"form.html")
def last(request):
    return render(request,"last.html")
