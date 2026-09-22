from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
