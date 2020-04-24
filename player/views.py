from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, View
from .models import Player

class HomeView(TemplateView):
     template_name = 'player/index.html'

     def get_context_data(self, *args, **kwargs):
          context = super().get_context_data(*args, **kwargs)
          context['players'] = Player.objects.all()
          return context