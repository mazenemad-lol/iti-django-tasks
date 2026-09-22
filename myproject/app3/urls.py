from django.urls import path
from . import views

app_name = 'app3'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_contact, name='create_contact'),
    path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
