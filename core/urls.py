from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^game_master$', GameMasterView.as_view(), name='game_master'),
    url(r'^player$', PlayerView.as_view(), name='player'),
]
