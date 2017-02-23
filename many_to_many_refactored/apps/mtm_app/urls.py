from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^showinterest/(?P<id>\d+)$', views.showInterest),
    url(r'^add_user$', views.add_user),
    url(r'^deleteuser/(?P<id>\d+)$', views.deleteUser),
    url(r'^showResults$', views.showResults),
    url(r'^deleteInterest/(?P<id>\d+)$', views.deleteInterest)
]
