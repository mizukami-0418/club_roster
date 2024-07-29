# teams/models.py

from django.db import models
from cloudinary.models import CloudinaryField

class Team(models.Model):
    DIVISION_CHOICES = [
        ('ND', '北地区'),
        ('ED', '東地区'),
        ('WD', '西地区'),
        ('SD', '南地区'),
    ]
    
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    founded = models.DateField()
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    image = CloudinaryField('image', resource_type='image', blank=True, null=True)
    
    # 野手所属数のカウント
    @property
    def field_player_count(self):
        return self.field_players.count()
    
    # 投手所属数のカウント
    @property
    def pitcher_count(self):
        return self.pitchers.count()
    
    def __str__(self):
        return self.name