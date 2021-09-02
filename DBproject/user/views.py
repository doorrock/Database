from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        user_id = request.POST.get('user_id',None)
        password = request.POST.get('password', None)
        name = request.POST.get('name', None)
        nick = request.POST.get('nick', None)
        age = request.POST.get('age', None)
        gender = request.POST.get('gender', None)
        score = request.POST.get('score', None)

        user = User(user_id=user_id, password=password, name=name, nick_name=nick, age=age, gender=gender, score=score)
        user.save()

        return redirect('/user/login/')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # if request.POST.get('signup',None)
        login_user_id = request.POST.get('user_id',None)
        login_password = request.POST.get('password', None)

        temp = User.objects.get(user_id=login_user_id)
        if login_password == temp.password:
            request.session['user_id'] = login_user_id
            request.session['user_pw'] = login_password
            return redirect('/user/user_main/')
        else:
            print("wrong password")
            return render(request, 'login.html')

def user_main(request):
    if request.method == "GET":
        return render(request, 'user_main.html')

def logout(request):
    request.session.modified=True
    del request.session['user_id']
    del request.session['user_pw']
    return redirect('/user/login/')