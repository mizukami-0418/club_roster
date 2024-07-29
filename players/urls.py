# players/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('player/<int:pk>/field_player/', views.field_player_detail, name='field_player_detail'),
    path('player/<int:pk>/pitcher/', views.pitcher_detail, name='pitcher_detail'),
    path('player/field_player_new/', views.field_player_new, name='field_player_new'),
    path('player/pitcher_new/', views.pitcher_new, name='pitcher_new'),
    path('player/<int:pk>/field_player_edit/', views.field_player_edit, name='field_player_edit'),
    path('player/<int:pk>/pitcher_edit/', views.pitcher_edit, name='pitcher_edit'),
    path('player/<int:pk>/field_player_delete/', views.field_player_delete, name='field_player_delete'),
    path('player/<int:pk>/pitcher_delete/', views.pitcher_delete, name='pitcher_delete'),
]
