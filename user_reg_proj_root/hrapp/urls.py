from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'hrapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='hrapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='hrapp/logout.html'), name='logout'),

]
