from django.conf.urls import url
from django.conf.urls import url
from .views import main
from .views import supergame

urlpatterns = [
    url(r'^$', main, name='main'),
    url('game', supergame, name='supergame')
]