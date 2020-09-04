from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.redirection, name='redirection'),
]