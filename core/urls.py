from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^game_master$', GameMasterView.as_view(), name='game_master'),

    url(r'^player_selection$', player_selection, name='player_selection'),
    url(r'^characters_panel$', characters_panel, name='characters_panel'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
