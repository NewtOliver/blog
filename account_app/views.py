from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        user_name = request.POST.get('用户名')
        password1 = request.POST.get('密码')
        password2 = request.POST.get('确认密码')

        try:
            # 判断用户名是否存在
            if User.objects.get(username=user_name):
                return render(request, 'signup.html', {"用户名错误": "该用户名已存在,请使用其他用户名"})
        except User.DoesNotExist:
            if password1 != password2:
                return render(request, 'signup.html', {'密码错误': '两次输入密码不一致，请重新输入密码'})
            else:
                User.objects.create_user(username=user_name, password=password1)
                return redirect('index')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        user_name = request.POST.get('用户名')
        password = request.POST.get('密码')
        user = auth.authenticate(username=user_name, password=password)
        
        if user is None:
            return render(request, 'signin.html', {'错误': '用户名或密码错误'})
        else:
            auth.login(request, user)
            return redirect('index')


def logout(request):
        auth.logout(request)
        return redirect('index')