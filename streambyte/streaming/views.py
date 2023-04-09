from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def home(request):
    return render(request, 'index.html')

# ----------------------
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        re_password=request.POST.get('re_password')
        
        # Validate data

        if password != re_password:
            return HttpResponse('passwords dont match')
        
        # Check if user with same username already exists
        _users = User.objects.filter(username=username)
        print(_users)
        if len(_users) != 0:
            return HttpResponse('User siwht same user name already exists')

        
        
        my_user=User.objects.create_user(username,email,password)
        my_user.save()

        return redirect('login')
    
    return render(request,'signup.html')

def login(request):
    if request.method=='POST' :
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("USername or Password is incorrect")
    return render(request, 'login.html')

def handlelogin(request):
    # BANAO GUDMARANI
    pass

def logout(request):
    return render('logout.html')

# ----------------------



def free(request):
    return render(request, 'free.html')

def paid(request):
    return render(request,'paid.html')

def forcreators(request):
    return render(request,'forcreators.html')

def contactus(request):
    # return HttpResponse("contact page")
    return render(request, 'contactus.html')

