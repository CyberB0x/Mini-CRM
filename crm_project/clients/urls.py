# clients/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('tasks/', views.task_list, name='task_list'),
]
