from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from Home.models import Register
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/loginuser')
    else:
        return render(request, 'index.html')

def register(request):
    if request.method =='POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Mobile = request.POST.get('Mobile')
        Password = request.POST.get('Password')
        Confirm_Password = request.POST.get('Confirm_Password')
        
        Studentregister = Register(Name = Name, Email = Email,Mobile = Mobile, Password = Password, Confirm_Password = Confirm_Password)
        
        Studentregister.save()
        user = User.objects.create_user(Email,Email, Password)
        user.save()
        return redirect('/loginuser')
    else:
        return render(request, 'register.html')
    
# def loginuser(request):
#     return render(request,'login.html')
    
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('Email')
        password = request.POST.get('Password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('username and password are incorrect')
    else:
         return render(request,'login.html')


