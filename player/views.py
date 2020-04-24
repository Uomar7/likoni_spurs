from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, View, ListView
from .models import Player

class PlayersList(ListView):
     model = Player
     template_name = 'players/index.html'
     context_object_name = 'players'