# players/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import FieldPlayer, Pitcher
from .forms import FieldPlayerForm, PitcherForm
from django.contrib import messages

# リスト
def player_list(request):
    field_players = FieldPlayer.objects.all()
    pitchers = Pitcher.objects.all()
    context = {
        'field_players': field_players,
        'pitchers': pitchers
    }
    return render(request, 'players/player_list.html', context)

# 詳細
def field_player_detail(request, pk):
    field_player = get_object_or_404(FieldPlayer, pk=pk)
    context = {'field_player': field_player,}
    return render(request, 'players/field_player_detail.html', context)

def pitcher_detail(request, pk):
    pitcher = get_object_or_404(Pitcher, pk=pk)
    context = {'pitcher': pitcher}
    return render(request, 'players/pitcher_detail.html', context)

# 新規登録
def field_player_new(request):
    if request.method == "POST":
        form = FieldPlayerForm(request.POST, request.FILES)
        if form.is_valid():
            field_player = form.save()
            messages.success(request, f'{ field_player.last_name } { field_player.first_name }選手が入団しました')
            return redirect('field_player_detail', pk=field_player.pk)
    else:
        form = FieldPlayerForm()
    return render(request, 'players/field_player_form.html', {'form': form})

def pitcher_new(request):
    if request.method == "POST":
        form = PitcherForm(request.POST, request.FILES)
        if form.is_valid():
            pitcher = form.save()
            messages.success(request, f'{ pitcher.last_name } { pitcher.first_name }投手が入団しました')
            return redirect('pitcher_detail', pk=pitcher.pk)
    else:
        form = PitcherForm()
    return render(request, 'players/pitcher_form.html', {'form': form})

# 編集
def field_player_edit(request, pk):
    field_player = get_object_or_404(FieldPlayer, pk=pk)
    if request.method == "POST":
        form = FieldPlayerForm(request.POST, request.FILES, instance=field_player)
        if form.is_valid():
            field_player = form.save()
            messages.success(request, f'{ field_player.last_name } { field_player.first_name }の情報を更新しました')
            return redirect('field_player_detail', pk=field_player.pk)
    else:
        form = FieldPlayerForm(instance=field_player)
    return render(request, 'players/field_player_form.html', {'form': form, 'field_player': field_player})

def pitcher_edit(request, pk):
    pitcher = get_object_or_404(Pitcher, pk=pk)
    if request.method == "POST":
        form = PitcherForm(request.POST, request.FILES, instance=pitcher)
        if form.is_valid():
            pitcher = form.save()
            messages.success(request, f'{ pitcher.last_name } {pitcher.first_name}の情報を更新しました')
            return redirect('pitcher_detail', pk=pitcher.pk)
    else:
        form = PitcherForm(instance=pitcher)
    return render(request, 'players/pitcher_form.html', {'form': form, 'pitcher': pitcher})

# 削除
def field_player_delete(request, pk):
    field_player = get_object_or_404(FieldPlayer, pk=pk)
    if request.method == "POST":
        field_player.delete()
        messages.success(request, '引退しました')
        return redirect('player_list')
    return render(request, 'players/field_player_confirm_delete.html', {'field_player': field_player})

def pitcher_delete(request, pk):
    pitcher = get_object_or_404(Pitcher, pk=pk)
    if request.method == "POST":
        pitcher.delete()
        messages.success(request, '引退しました')
        return redirect('player_list')
    return render(request, 'players/pitcher_confirm_delete.html', {'pitcher': pitcher})
