from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LobbyView(TemplateView):
    template_name = 'chat/index.html'


class Room(TemplateView):
    template_name = 'chat/room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_name'] = self.kwargs.pop('room_name', None)
        return context

