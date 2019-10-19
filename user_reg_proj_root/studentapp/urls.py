from django.urls import path
from .views import student_register, course_view, each_course
from django.contrib.auth import views as auth_views

app_name = 'studentapp'

urlpatterns = [
    path('', student_register, name='student_register'),
    path('view/', course_view, name='course_view'),
    path('<int:course_id>', each_course, name='each_course'),
    path('login/', auth_views.LoginView.as_view(template_name='studentapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='studentapp/logout.html'), name='logout'),
]
