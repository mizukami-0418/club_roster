# players/sample_data.py

import random
import os
from datetime import date, timedelta
from players.models import FieldPlayer, Pitcher
from teams.models import Team
from dotenv import load_dotenv

load_dotenv()

FIRST_NAMES = [
    "蓮", "蒼", "樹", "陽翔", "悠真", "湊", "悠斗", "陽向", "大和", "颯太",
    "結翔", "朝陽", "伊織", "新", "優", "結人", "一颯", "悠", "悠翔", "陸",
    "湊斗", "陽太", "瑛太", "颯", "律", "凛太郎", "昴", "柊斗", "朔太郎", "結",
    "悠人", "奏太", "蒼真", "晴", "直哉", "仁", "空", "大輝", "匠", "陽",
    "颯人", "蓮斗", "涼", "瞬", "勇斗", "咲良", "翔", "陽仁", "悠斗", "奏汰",
    "柊", "瞬太", "陸斗", "陽翔", "涼太", "太陽", "瑛斗", "律斗", "陽生", "結大",
    "一真", "空斗", "颯真", "玲央", "空大", "晴斗", "智樹", "壮真", "隼", "陽樹",
    "楓", "天翔", "琉生", "優真", "蒼空", "湊大", "颯斗", "颯汰", "律希", "陽真",
    "悠太", "結斗", "瑛士", "蒼汰", "悠翔", "悠輝", "優斗", "昴太", "楓真", "湊斗",
    "瑛太", "涼真", "颯希", "律真", "樹斗", "陽光", "優樹", "悠仁", "昊", "蓮生"
]

LAST_NAMES = [
    "佐藤", "鈴木", "高橋", "田中", "伊藤", "渡辺", "山本", "中村", "小林", "加藤",
    "吉田", "山田", "佐々木", "松本", "井上", "木村", "林", "斎藤", "清水", "山口",
    "池田", "阿部", "森", "橋本", "山崎", "石川", "前田", "藤田", "小川", "岡田",
    "後藤", "長谷川", "村上", "近藤", "石井", "斉藤", "坂本", "遠藤", "青木", "藤井",
    "西村", "福田", "太田", "三浦", "岡本", "松田", "中川", "中島", "原田", "小野",
    "田村", "竹内", "金子", "和田", "中野", "石田", "上田", "森田", "原", "柴田",
    "酒井", "工藤", "横山", "宮崎", "宮本", "内田", "高木", "谷口", "安藤", "今井",
    "丸山", "大野", "高田", "福島", "藤原", "河野", "武田", "菅原", "小島", "田口",
    "永井", "土屋", "松井", "木下", "野口", "大西", "杉山", "新井", "三宅", "浜田",
    "市川", "水野", "桜井", "久保", "川口", "吉川", "山内", "平野", "久保田", "吉村"
]

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def create_field_players(teams):
    POSITIONS = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH']
    players = []
    cloudinary_image = os.getenv('CLOUDINARY_IMAGE')
    for _ in range(640):
        last_name = random.choice(LAST_NAMES)
        first_name = random.choice(FIRST_NAMES)
        team = random.choice(teams)
        position = random.choice(POSITIONS)
        birth_date = random_date(date(1990, 4, 1), date(2005, 12, 31))
        height = random.randint(170, 195)
        weight = random.randint(70, 100)
        batting_average = round(random.uniform(0.220, 0.399), 3)
        homeruns = random.randint(0, 80)
        image = cloudinary_image
        player = FieldPlayer(
            first_name=first_name,
            last_name=last_name,
            team=team,
            position=position,
            birth_date=birth_date,
            height=height,
            weight=weight,
            batting_average=batting_average,
            homeruns=homeruns,
            image=image,
        )
        players.append(player)
    FieldPlayer.objects.bulk_create(players)

def create_pitchers(teams):
    POSITIONS = ['SP', 'RP', 'SU', 'CL']
    players = []
    cloudinary_image = os.getenv('CLOUDINARY_IMAGE')
    for _ in range(480):
        last_name = random.choice(LAST_NAMES)
        first_name = random.choice(FIRST_NAMES)
        team = random.choice(teams)
        position = random.choice(POSITIONS)
        birth_date = random_date(date(1990, 4, 1), date(2005, 12, 31))
        height = random.randint(170, 210)
        weight = random.randint(70, 110)
        earned_run_average = round(random.uniform(0.10, 4.99), 2)
        image = cloudinary_image
        player = Pitcher(
            first_name=first_name,
            last_name=last_name,
            team=team,
            position=position,
            birth_date=birth_date,
            height=height,
            weight=weight,
            earned_run_average=earned_run_average,
            image=image,
        )
        players.append(player)
    Pitcher.objects.bulk_create(players)

def generate_sample_data():
    teams = Team.objects.all()
    create_field_players(teams)
    create_pitchers(teams)
