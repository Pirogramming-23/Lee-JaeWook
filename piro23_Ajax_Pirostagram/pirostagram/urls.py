from django.urls import path
from . import views

app_name = 'pirostagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/like/', views.post_like, name='post_like'),
    path('comment/create/', views.comment_create, name='comment_create'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]
