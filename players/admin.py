# players/admin.py

from django.contrib import admin
from .models import FieldPlayer, Pitcher

@admin.register(FieldPlayer)
class FieldPlayerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'team', 'position', 'batting_average', 'homeruns')
    list_filter = ('team', 'position')
    search_fields = ('last_name', 'first_name')
    ordering = ('last_name', 'first_name')

@admin.register(Pitcher)
class PitcherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'team', 'position', 'earned_run_average')
    list_filter = ('team', 'position')
    search_fields = ('last_name', 'first_name')
    ordering = ('last_name', 'first_name')
