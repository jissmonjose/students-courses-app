from . import views
from django.urls import path
# import views for login and logout features
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin_home/', views.home, name='home'),
    path('', views.index_page, name='index_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact, name='contact'),
    path('view_students/', views.view_students, name='view_students'),
    path('<int:stud_id>', views.each_student_details, name='each_student_details'),
    path('login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name='logout'),

]
