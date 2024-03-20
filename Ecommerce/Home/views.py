from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')

def card(request):
    return render(request, 'card.html')
