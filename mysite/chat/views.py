from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LobbyView(TemplateView):
    template_name = 'chat/lobby.html'
