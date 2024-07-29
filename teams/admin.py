# teams/admin.py

from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'founded', 'division', 'field_player_count', 'pitcher_count')
    list_filter = ('division', 'founded')
    search_fields = ('name', 'city')
    ordering = ('division',)
    fields = ('name', 'city', 'founded', 'division')
    readonly_fields = ('field_player_count', 'pitcher_count')
