from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^showinterest/(?P<id>\d+)$', views.showinterest),
    url(r'^process$', views.formProcess),
]
