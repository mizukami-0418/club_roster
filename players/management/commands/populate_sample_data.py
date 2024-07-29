# players/management/commands/populate_sample_data.py

from django.core.management.base import BaseCommand
from players.sample_data import generate_sample_data

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        generate_sample_data()
        self.stdout.write(self.style.SUCCESS('サンプルデータの作成に成功しました'))
