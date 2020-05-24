from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import register
from django.urls import reverse
from django.core import serializers
import hashlib

# Create your views here.
def ulogin(request):
    cond=False
    if request.method=='POST':
        uname=request.POST['user']
        password=request.POST['pswd']
        pswd=hashlib.sha512(password.encode())
        print(uname)
        print(password)
        user=register.objects.get(username=uname,passwd=pswd.hexdigest())
        if user.username==uname:
            if user is not None:
                request.session['username'] = user.username
                request.session['userId']=user.id
            #    return redirect(reverse('/accounts/u_account', kwargs={"userId": user.id}))
                return redirect('/accounts/u_account')
            else:
                cond=True
                messages.info(request,'Invalid Username or Password')
                return redirect('user_login')
    return render(request,'user_login.html',{'cond':cond})

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        username=request.POST['username']
        dob=request.POST['birth']
        gender=request.POST['gender']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=hashlib.sha512(password1.encode())
        if password1==password2:
            user=register(username=username, passwd=password.hexdigest(), email=email, firstname=first_name, lastname=last_name, d_o_b=dob, 
            gender=gender, mobile=mobile)
            user.save()
            print('User Created')

        else:
            print('Password not matching')

    else:
        return render(request,'register.html')
    return redirect('/')

def index(request):
    return render(request, "index.html")
