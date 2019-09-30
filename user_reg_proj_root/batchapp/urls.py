from django.urls import path
from . import views

urlpatterns = [
    path('', views.batch, name='batch'),
    path('batches/', views.batch_list, name='batch_list'),
]


