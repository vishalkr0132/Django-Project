from Home import views
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('register_user', views.register, name='register'),
    path('loginuser', views.loginuser, name='login'),
]