from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainer_create, name='trainer_create'),
    path('trainers/', views.TrainersList.as_view(), name='trainer_view'),
    path('<int:pk>', views.TrainerDetail.as_view(), name='trainer_one'),
    path('delete/<int:pk>', views.TrainerDelete.as_view(), name='trainer_delete'),
    path('edit/<int:pk>', views.TrainerEdit.as_view(), name='trainer_edit'),
]
