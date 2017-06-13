import re

from django.shortcuts import render
from django.views import generic

from .models import Rifugio, Gruppo, Pagina, Paragrafo, LayoutCampo



class ListaView(generic.ListView):
    template_name = 'infomont_app/homepage.html'
   
    def get_queryset(self):
        """Ritorna la lista dei rifugi."""
        return Rifugio.objects.order_by('nome')
        
    
    def get_context_data(self, **kwargs):
        """ Ritorna il contesto della pagina """
        context = super(ListaView, self).get_context_data(**kwargs)
        context['title'] = "Lista Rifugi"
        context['home'] = 'lista'
        return context


class MappaView(generic.ListView):
    template_name = 'infomont_app/mappa_rifugi.html'
   
    def get_queryset(self):
        """Ritorna la lista dei rifugi."""
        return Rifugio.objects.order_by('nome')
        
    
    def get_context_data(self, **kwargs):
        """ Ritorna il contesto della pagina """
        context = super(MappaView, self).get_context_data(**kwargs)
        context['title'] = "Mappa Rifugi"
        context['home'] = 'mappa'
        return context



class RifugioView(generic.DetailView):
    model = Rifugio
    template_name = 'infomont_app/dati_rifugio.html'
    
    def get_context_data(self, **kwargs):
        """ Ritorna il contesto della pagina """
        context = super(RifugioView, self).get_context_data(**kwargs)
        
        pagina_url = self.kwargs['pagina']
        nome_pagina = " ".join([a for a in re.findall('[A-Z][^A-Z]*', pagina_url)])
        
        gruppi = [ {'nome': gruppo.nome, 'pagine': Pagina.objects.filter(gruppo__nome=gruppo.nome) } for gruppo in Gruppo.objects.all() if gruppo.nome != "Barra"]
        
        campi_barra = [ {
                            'nome': campo.nome,
                            'valore': Rifugio.objects.filter(nome = context['rifugio'].nome)[0].__dict__[campo.etichetta]
                        } 
                        for campo in LayoutCampo.objects.filter(paragrafo__nome='Barra')]
        
        print(context)
        paragrafi = [ { 'nome': paragrafo.nome, 
                        'campi': [{
                                    'nome': campo.nome,
                                    'valore': Rifugio.objects.filter(nome = context['rifugio'].nome)[0].__dict__[campo.etichetta]
                                  }   
                                  for campo in LayoutCampo.objects.filter(paragrafo__nome=paragrafo.nome)]
                      } for paragrafo in Paragrafo.objects.filter(pagina__nome=nome_pagina)]
                      
        
        context['title'] = "{} - {}".format(nome_pagina, context['rifugio'])
        context['nome_pagina'] = nome_pagina
        context['gruppi'] = gruppi
        context['campi_barra'] = campi_barra
        context['paragrafi'] = paragrafi
        
        context['latitudine'] = 46.3093808
        context['longitudine'] = 9.7374249
        
        return context
        
        
        
        
    # Metodo di debug, poi rimuovimi
    def cut_date(self, field):
        if field.verbose_name.split(" ")[0] == "Data":
            return field.value_to_string(self.object)[:10]
        return field.value_to_string(self.object)

