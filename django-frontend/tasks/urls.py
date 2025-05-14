from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<str:task_id>/edit/', views.task_edit, name='task_edit'),
    path('task/<str:task_id>/delete/', views.task_delete, name='task_delete'),
    path('task/<str:task_id>/move/<str:direction>/', views.task_move, name='task_move'),
]
