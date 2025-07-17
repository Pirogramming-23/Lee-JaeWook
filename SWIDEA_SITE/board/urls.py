# board/urls.py
from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('create/', views.idea_create, name='idea_create'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('<int:pk>/update/', views.idea_update, name='idea_update'),
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('ideas/<int:pk>/increase_interest/', views.increase_interest, name='increase_interest'),
    path('ideas/<int:pk>/decrease_interest/', views.decrease_interest, name='decrease_interest'),
    path('ideas/<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
    path('devtools/<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('devtools/<int:pk>/update/', views.devtool_update, name='devtool_update'),
    path('devtools/<int:pk>/delete/', views.devtool_delete, name='devtool_delete'),

]


urlpatterns += [
    path('devtools/create/', views.devtool_create, name='devtool_create'),
    path('devtools/', views.devtool_list, name='devtool_list'),
]
