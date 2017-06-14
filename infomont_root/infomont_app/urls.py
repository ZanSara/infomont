from django.conf.urls import url

from . import views

app_name = 'infomont'

urlpatterns = [
    url(r'^$', views.ListaView.as_view(), name='home'),
    url(r'^lista$', views.ListaView.as_view(), name='lista'),
    url(r'^mappa$', views.MappaView.as_view(), name='mappa'),
    url(r'^rifugi/(?P<pk>[0-9]+)/Immagini$', views.ImmaginiView.as_view(), name='upload_immagini'),
    url(r'^rifugi/(?P<pk>[0-9]+)/(?P<pagina>\w+)$', views.RifugioView.as_view(), name='dettagli_rifugio'),
    url(r'^rifugi/(?P<pk>[0-9]+)/(?P<pagina>\w+)/edit$', views.RifugioFormView.as_view(), name='edit_dettagli_rifugio'),
]

