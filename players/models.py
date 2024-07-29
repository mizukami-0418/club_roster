# players/models.py

from django.db import models
from teams.models import Team
from cloudinary.models import CloudinaryField

class FieldPlayer(models.Model):
    POSITION_CHOICES = [
        ('C', '捕手'),
        ('1B', '一塁手'),
        ('2B', '二塁手'),
        ('3B', '三塁手'),
        ('SS', '遊撃手'),
        ('LF', '左翼手'),
        ('CF', '中堅手'),
        ('RF', '右翼手'),
        ('DH', '指名打者'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='field_players')
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    birth_date = models.DateField()
    height = models.IntegerField(help_text='cmで入力してください')
    weight = models.IntegerField(help_text='kgで入力してください')
    batting_average = models.FloatField()
    homeruns = models.IntegerField()
    image = CloudinaryField('image', resource_type='image', blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Pitcher(models.Model):
    POSITION_CHOICES = [
        ('SP', '先発'),
        ('RP', '中継ぎ'),
        ('SU', 'セットアッパー'),
        ('CL', 'クローザー'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='pitchers')
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    birth_date = models.DateField()
    height = models.IntegerField(help_text='cmで入力してください')
    weight = models.IntegerField(help_text='kgで入力してください')
    earned_run_average = models.FloatField()
    image = CloudinaryField('image', resource_type='image', blank=True, null=True)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"