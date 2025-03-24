from django.shortcuts import render
from .models import Player, Game

def home(request):
    games = Game.objects.all()
    return render(request, 'chess/home.html', {'games': games})
