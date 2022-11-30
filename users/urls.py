from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as authentication_views

app_name ='users'

urlpatterns = [
path('',views.register,name='register'),
#path('login/',authentication_views.LoginView.as_view(template_name='loggin.html'),name='login'),
path('login/', views.login_attempt, name='login'),
path('logout/',authentication_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
#path('createprofile/', views.create_profile, name = 'createprofile'),
path('profile/', views.profile, name='profile'),
path('update/<int:id>', views.update, name= 'update'),

path('taken/', views.taken, name = 'taken'),
path('error/', views.error_page, name = 'error'),

path('token' , views.token_send , name="token_send"),
path('regsuccess' , views.regsuccess , name='regsuccess'),
path('verify/<auth_token>', views.verify , name="verify")
]
