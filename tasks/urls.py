from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('project/create/', views.create_project, name='create_project'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('task/<int:pk>/toggle/', views.toggle_task_status, name='toggle_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:pk>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:pk>/toggle/', views.toggle_task_status, name='toggle_task_status'),
]

