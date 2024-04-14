from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='logout'),
    path('register/',views.register, name='register'),
    path('tasks/',views.tasks, name='tasks'),
    path('create_task/',views.create_task, name='create_task'),
    path('get_task/<int:task_id>/', views.get_task, name='get_tasks'),
    path('update_task/<int:task_id>/', views.update_task, name='update_tasks'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_tasks'),
]