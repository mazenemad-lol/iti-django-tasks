from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_article, name='create_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
]
