from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'core/index.jinja'

    def get_context_data(self, **kwargs):
        kwargs = super(IndexView, self).get_context_data(**kwargs)
        kwargs['players'] = []
        return kwargs

class PlayerView(TemplateView):
    template_name = 'core/player.jinja'


class GameMasterView(TemplateView):
    template_name = 'core/game_master.jinja'
