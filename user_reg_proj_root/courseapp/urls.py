from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_create, name='course_create'),
    path('courses/', views.course_list, name='course_list'),
    path('<int:pk>', views.each_courses, name='each_courses'),
    path('edit/<int:pk>', views.course_update, name='course_update'),

]
