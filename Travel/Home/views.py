from urllib import request
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render (request,'services.html')

def packages(request):
    return render (request,'packages.html')

def contact(request):
    return render (request,'contact.html')

def booking(request):
    return render (request,'booking.html')