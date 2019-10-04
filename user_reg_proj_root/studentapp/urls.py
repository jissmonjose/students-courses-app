from django.urls import path
from .views import student_register, course_view, each_course

urlpatterns = [
    path('', student_register, name='student_register'),
    path('view/', course_view, name='course_view'),
    path('<int:course_id>', each_course, name='each_course'),
]
