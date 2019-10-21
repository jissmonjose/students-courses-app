from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_create, name='course_create'),
    path('course/', views.course_list, name='course_list'),
    path('<int:pk>', views.each_courses, name='each_courses'),
    path('delete/<int:pk>', views.CourseDelete.as_view(), name='course_delete'),
    path('edit/<int:pk>', views.CourseEdit.as_view(), name='course_edit'),
]

