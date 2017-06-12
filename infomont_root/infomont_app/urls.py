from django.conf.urls import url

from . import views

app_name = 'infomont'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='list'),
    url(r'^lista$', views.IndexView.as_view(), name='list'),
    url(r'^mappa$', views.IndexView.as_view(), name='list'), # cambiami quando la mappa va
    url(r'^rifugi/(?P<pk>[0-9]+)/main$', views.DetailView.as_view(), name='details'),
]

