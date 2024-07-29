# teams/forms.py

from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'city', 'founded', 'division', 'image']
        labels = {
            'name': 'チーム名',
            'city': 'ホームタウン',
            'founded': '設立',
            'division': '地区',
            'image': 'チームロゴ'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '北海道ブリザーズ', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': '札幌市', 'class': 'form-control'}),
            'founded': forms.DateInput(attrs={'placeholder': '2000-01-01', 'class': 'form-control'}),
            'division': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
