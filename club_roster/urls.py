"""
URL configuration for club_roster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

# カスタムエラーハンドラ
handler404 = 'error.views.custom_404'
handler500 = 'error.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('teams/', include('teams.urls')),
    path('players/', include('players.urls')),
    path('contact/', include('contact.urls')),
    path('trigger-500/', views.trigger_500, name='trigger500'), # 500エラーを発生させるためのルート
]
