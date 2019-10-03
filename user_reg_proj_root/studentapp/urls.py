from django.urls import path
from .views import student_register, course_view

urlpatterns = [
    path('', student_register, name='student_register'),
    path('view/', course_view, name='course_view'),
]
