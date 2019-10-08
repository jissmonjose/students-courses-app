from django.urls import path
from . import views

urlpatterns = [
    path('', views.batch, name='batch'),
    path('batches/', views.batch_list, name='batch_list'),
    path('batches/<int:pk>', views.each_batch, name='each_batch'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name="batch_delete"),
    path('edit/<int:pk>', views.UpdateView.as_view(), name='batch_edit'),
]


