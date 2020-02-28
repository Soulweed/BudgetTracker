from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,get_user,login
import json


# Create your views here.

def login_func(request):
    if request.method == 'POST':
        # get data from = request 
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # return render(request, 'detail.html')
            return redirect('/addincome/')
        else:
            return render(request, 'login.html')
    
    elif request.method == 'GET':
        print('GET Method Recevie')
        return render(request, 'login.html')