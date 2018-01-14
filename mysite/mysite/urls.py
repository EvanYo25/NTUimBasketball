"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from basketR import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^team$', views.listteam, name='team'),
    url(r'^listrecord$', views.listrecord),
    url(r'^record/(?P<tID>\d+)/$', views.detail, name='teamDetail'),
    url(r'^record/(?P<tID>\d+)/(?P<cID>\d+)/$', views.record, name='teamRecord'),
    url(r'^record/(?P<tID>\d+)/newGame/$', views.addGame, name='addGame'),
    url(r'^record/(?P<tID>\d+)/newGDetail/$', views.gameDetail, name='GDetail'),

    url(r'^addPlayer/(?P<id>\d)/$', views.addPlayer),
    url(r'^DELplayer/(?P<pID>\d)/$', views.delPlayer, name='DELplayer'),
    url(r'^welcome/$', views.welcome),
    # url(r'^addPlayer$', views.addPlayer),
    # url(r'^create/$', 'views.addPlayer'),
]
