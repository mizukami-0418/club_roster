# teams/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('team/<int:pk>/', views.team_detail, name='team_detail'),
    path('team/new/', views.team_new, name='team_new'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),
]
