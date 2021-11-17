from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
import sys
 
# 시스템 인코딩 설정의 출력
 
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("success")
            login(request, user)
        else:
            print("fail")
        
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login")


# def signup_view(request):
    
#     if request.method =="POST":
#         print(request.POST)
#         username = request.POST["username"]
#         password = request.POST["password"]
#         name = request.POST["name"]
    
#         user = User.objects.create_user(username, password, name)
#         # user.last_name = lastname
#         user.save()
#         return redirect("user:login")
#     return render(request, "users/signup.html")

def signup_view(request):
    if request.method == "GET":
        return render(request, 'users/signup.html')

    elif request.method == "POST":
        username = request.POST.get('username',None)   #딕셔너리형태
        name = request.POST.get('name',None)
        gender  = request.POST.get('gender  ',None)
        height = request.POST.get('height',None)
        weight = request.POST.get('weight',None)
        age = request.POST.get('age_category',None)
        activity = request.POST.get('activity',None)
        password = request.POST.get('pw',None)
        re_password = request.POST.get('re_password',None)
        res_data = {} 
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = User(username=username, password=make_password(password))
            user.name   = name
            user.gender = gender
            user.height = height
            user.weight = weight
            user.age = age
            user.activity = activity
            user.save()
            return redirect("user:login")
        return render(request, 'users/signup.html', res_data) #register를 요청받으면 register.html 로 응답.