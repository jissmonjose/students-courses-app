from django.urls import path
from . import views

urlpatterns = [
    path('', views.batch, name='batch'),
    path('batches/', views.batch_list, name='batch_list'),
    path('<int:batch_id>', views.each_batch, name='each_batch'),
    path('edit/<int:pk>', views.BatchEdit.as_view(), name='edit_batch'),
]


