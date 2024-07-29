# players/forms.py

from django import forms
from .models import FieldPlayer, Pitcher

class FieldPlayerForm(forms.ModelForm):
    
    class Meta:
        model = FieldPlayer
        fields = [
            'last_name', 'first_name', 'team', 'position', 'birth_date', 'height', 'weight', 'batting_average', 'homeruns', 'image'
            ]
        labels = {
            'last_name': '姓',
            'first_name': '名',
            'team': '所属',
            'position': 'ポジション',
            'birth_date': '誕生日',
            'height': '身長',
            'weight': '体重',
            'batting_average': '打率',
            'homeruns': '本塁打',
            'image': 'プロフィール画像',
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': '山田', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': '太郎', 'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-select'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
            'birth_date': forms.DateInput(attrs={'placeholder': '2000-01-01', 'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'placeholder': '180', 'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'placeholder': '75', 'class': 'form-control'}),
            'batting_average': forms.NumberInput(attrs={'placeholder': '0.300', 'class': 'form-control'}),
            'homeruns': forms.NumberInput(attrs={'placeholder': '30', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}), 
        }

class PitcherForm(forms.ModelForm):
    
    class Meta:
        model = Pitcher
        fields = [
            'last_name', 'first_name', 'team', 'position', 'birth_date', 'height', 'weight', 'earned_run_average', 'image'
            ]
        labels = {
            'last_name': '姓',
            'first_name': '名',
            'team': '所属',
            'position': 'ポジション',
            'birth_date': '誕生日',
            'height': '身長',
            'weight': '体重',
            'earned_run_average': '防御率',
            'image': 'プロフィール画像',
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': '山田', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': '太郎', 'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-select'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
            'birth_date': forms.DateInput(attrs={'placeholder': '2000-01-01', 'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'placeholder': '180', 'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'placeholder': '75', 'class': 'form-control'}),
            'earned_run_average': forms.NumberInput(attrs={'placeholder': '3.00', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }