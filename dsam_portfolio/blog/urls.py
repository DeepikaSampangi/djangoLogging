from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from .views import allblogs, blog_details

urlpatterns = [
    path('',allblogs, name='blog_home'),
    path('<int:blog_id>', blog_details, name='blog_details')
]
