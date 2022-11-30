from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as authentication_views

app_name ='exam'

urlpatterns = [
path('exam/<int:id>', views.exam, name='exam'),
path('success/',views.success, name='success'),
path('error/', views.error, name='error'),
path('newexam/<int:id>', views.newexam, name='newexam'),
path('instruct', views.instruct, name='instruct'),
    
]



