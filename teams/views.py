# teams/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Team
from .forms import TeamForm
from django.contrib import messages

# リスト
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

# 詳細
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'teams/team_detail.html', {'team': team})

# 新規登録
def team_new(request):
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save()
            messages.success(request, '新球団が誕生しました')
            return redirect('team_detail', pk=team.pk)
    else:
        form = TeamForm()
    return render(request, 'teams/team_form.html', {'form': form})

# 編集
def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            team = form.save()
            messages.success(request, f'{ team.name }の情報を更新しました')
            return redirect('team_detail', pk=team.pk)
    else:
        form = TeamForm(instance=team)
    return render(request, 'teams/team_form.html', {'form': form, 'team': team})

# 削除
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        team.delete()
        messages.success(request, 'チームが解散しました')
        return redirect('team_list')
    return render(request, 'teams/team_confirm_delete.html', {'team': team})
