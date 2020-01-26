
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('',views.registration,name='registration'),
    path('login',views.Login,name='login'),
    path('loginpage',views.loginPage,name='loginpage'),

]
