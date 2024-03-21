from Home import views
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('packages', views.packages, name='packages'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    
]