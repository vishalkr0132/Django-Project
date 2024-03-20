from Home import views
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='home' ),
    path('product', views.product, name='product' ),
    path('contact', views.contact, name='contact' ),
    path('card', views.card, name='card' ),



]