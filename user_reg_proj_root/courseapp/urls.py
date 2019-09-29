from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_create, name='course_create'),
    path('courses/', views.course_list, name='course_list'),
    path('<int:course_id>', views.each_courses, name='each_courses'),
]
