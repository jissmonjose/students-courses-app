from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainer_create, name='trainer_create'),
    path('trainers/', views.trainer_view, name='trainer_view'),
    path('<int:trainer_id>', views.trainer_one, name='trainer_one'),
]
