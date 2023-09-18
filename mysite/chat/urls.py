from django.urls import path

from . import views

urlpatterns = [path('', views.LobbyView.as_view(), name='lobby'),
               path('<str:room_name>/', views.Room.as_view(), name='room'),
               ]
