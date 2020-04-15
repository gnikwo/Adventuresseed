from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.views.generic import TemplateView

from core.models import *

class IndexView(TemplateView):
    template_name = 'core/index.jinja'

    def get_context_data(self, **kwargs):
        kwargs = super(IndexView, self).get_context_data(**kwargs)
        try:
            game = Game.objects.filter(active=True)[0]
            kwargs['game_selected'] = True
            kwargs['game'] = game
        except IndexError as e:
            kwargs['game_selected'] = False
        return kwargs

class GameMasterView(TemplateView):
    template_name = 'core/index.jinja'

    def get_context_data(self, **kwargs):
        kwargs = super(GameMasterView, self).get_context_data(**kwargs)
        kwargs['game_master'] = True
        kwargs['games'] = Game.objects.order_by('last_played_date')
        return kwargs

def player_selection(request):
    kwargs = {}
    try:
        game = Game.objects.filter(active=True)[0]
        kwargs['game_selected'] = True
        kwargs['game'] = game
    except IndexError as e:
        kwargs['game_selected'] = False
    return render(request, 'core/player_selection.jinja', kwargs)

def characters_panel(request):
    kwargs = {}
    try:
        game = Game.objects.filter(active=True)[0]
        kwargs['game_selected'] = True
    except IndexError as e:
        kwargs['game_selected'] = False
    return render(request, 'core/characters_panel.jinja', kwargs)
