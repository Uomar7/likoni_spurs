from django.shortcuts import render,get_object_or_404, get_list_or_404
from .models import Player
from django.views.generic import (
     ListView,
     DetailView,
)


class PlayersList(ListView):
     model = Player
     template_name = 'players/index.html'
     context_object_name = 'players'

class PlayerDetail(DetailView):
     model = Player
     template_name = 'players/player_detail.html'
     context_object_name = 'player'