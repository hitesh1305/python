from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.blog_create, name='blog_create'),
    path('edit/<int:post_id>/', views.blog_edit, name='blog_edit'),
    path('delete/<int:post_id>/', views.blog_delete, name='blog_delete'),
]
