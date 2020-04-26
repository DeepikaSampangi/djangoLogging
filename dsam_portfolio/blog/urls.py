from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from .views import allblogs

urlpatterns = [
    path('',allblogs, name='blog_home')
]
