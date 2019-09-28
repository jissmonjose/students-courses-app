from . import views
from django.urls import path
# import views for login and logout features
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name='logout'),

]
