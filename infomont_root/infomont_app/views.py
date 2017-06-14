import re, collections

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.forms import modelformset_factory

from .models import Rifugio, Gruppo, Pagina, Paragrafo, LayoutCampo
from .forms import UploadFileForm, RifugioForm



class ListaView(generic.ListView):
    template_name = 'infomont_app/homepage.html'
   
    def get_queryset(self):
        """Ritorna la lista dei rifugi."""
        return Rifugio.objects.order_by('nome')
        # Visualizza rifugi diversi in base al login (in get_queryset)
        #if self.kwargs['pk'] == self.request.user.id:
        #    return Rifugio.objects.filter(id=self.request.user.id)
        #else:
        #    return Rifugio.objects.none()
        
    
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
        # Visualizza rifugi diversi in base al login (in get_queryset)
        #if self.kwargs['pk'] == self.request.user.id:
        #    return Rifugio.objects.filter(id=self.request.user.id)
        #else:
        #    return Rifugio.objects.none()
        
    
    def get_context_data(self, **kwargs):
        """ Ritorna il contesto della pagina """
        context = super(MappaView, self).get_context_data(**kwargs)
        context['title'] = "Mappa Rifugi"
        context['home'] = 'mappa'
        
        context['coordinate'] = []
        for rifugio in Rifugio.objects.all():
            context['coordinate'].append( {'rifugio': rifugio.nome, 'id':rifugio.id, 'lat': rifugio.latitudine,'lng': rifugio.longitudine } )
            
        print(context['coordinate'])
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
        
        paragrafi = [ { 'nome': paragrafo.nome, 
                        'campi': [{
                                    'nome': campo.nome,
                                    'valore': Rifugio.objects.filter(nome = context['rifugio'].nome)[0].__dict__[campo.etichetta]
                                  }   
                                  for campo in LayoutCampo.objects.filter(paragrafo__id=paragrafo.id)]
                      } for paragrafo in Paragrafo.objects.filter(pagina__nome=nome_pagina)]
                      
        
        context['title'] = "{} - {}".format(nome_pagina, context['rifugio'])
        context['nome_pagina'] = nome_pagina
        context['pagina_url'] = pagina_url
        context['gruppi'] = gruppi
        context['campi_barra'] = campi_barra
        context['paragrafi'] = paragrafi
        
        if nome_pagina == "Dati Geografici":
            context['latitudine'] = Rifugio.objects.filter(nome = context['rifugio'].nome)[0].__dict__['latitudine']
            context['longitudine'] = Rifugio.objects.filter(nome = context['rifugio'].nome)[0].__dict__['longitudine']
        
        return context
        
    # Metodo di debug, poi rimuovimi
    def cut_date(self, field):
        if field.verbose_name.split(" ")[0] == "Data":
            return field.value_to_string(self.object)[:10]
        return field.value_to_string(self.object)
        
        
        
        
        
        
        
        
class RifugioFormView(generic.UpdateView):
    model = Rifugio
    form = RifugioForm
    fields = '__all__'
    template_name = 'infomont_app/dati_rifugio_form.html'
    
    
    def __init__(self, *args, **kwargs):
        super(RifugioFormView, self).__init__(*args, **kwargs)
        
        
    def dispatch(self, request, *args, **kwargs):
        #print(self.kwargs['pagina'])
        nomepagina = " ".join([a for a in re.findall('[A-Z][^A-Z]*', self.kwargs['pagina'] )])
        
        paragrafi = [ [campo.etichetta for campo in LayoutCampo.objects.filter(paragrafo__nome=paragrafo.nome)]
                       for paragrafo in Paragrafo.objects.filter(pagina__nome=nomepagina)]
        campi = sum(paragrafi, [])
        
        print(self.fields)
        
        #nuovi_campi = collections.OrderedDict()
        #for fieldname, fieldvalue in self.fields.items():
        #    if fieldname in campi:
        #        nuovi_campi[fieldname] = fieldvalue
        
        self.fields = campi#nuovi_campi
        
        return super().dispatch(request, *args, **kwargs)
        
        
    def get_fields(self):
        
        print(self.kwargs['pagina'])
        nomepagina = " ".join([a for a in re.findall('[A-Z][^A-Z]*', self.kwargs['pagina'] )])
        
        paragrafi = [ [campo.etichetta for campo in LayoutCampo.objects.filter(paragrafo__nome=paragrafo.nome)]
                       for paragrafo in Paragrafo.objects.filter(pagina__nome=nomepagina)]
        campi = sum(paragrafi, [])
        
        nuovi_campi = collections.OrderedDict()
        for fieldname, fieldvalue in self.fields.items():
            if fieldname in campi:
                nuovi_campi[fieldname] = fieldvalue
        
        self.fields = nuovi_campi
        return nuovi_campi
        
    
    def get_success_url(self):
        return '/rifugi/{}/{}'.format(self.kwargs['pk'], self.kwargs['pagina'])
 
    def get_context_data(self, **kwargs):
        """ Ritorna il contesto della pagina """
        
        context = super(RifugioFormView, self).get_context_data(**kwargs)
        
        context['url_pagina'] = self.kwargs['pagina']
        context['nome_pagina'] = " ".join([a for a in re.findall('[A-Z][^A-Z]*', self.kwargs['pagina'])])
        context['title'] = "Edit '{}'".format(context['nome_pagina'], context['rifugio'])
        
        gruppi = [ {'nome': gruppo.nome, 'pagine': Pagina.objects.filter(gruppo__nome=gruppo.nome) } for gruppo in Gruppo.objects.all() if gruppo.nome != "Barra"]
        campi_barra = [ {
                            'nome': campo.nome,
                            'valore': Rifugio.objects.filter(nome = context['rifugio'].nome)[0].__dict__[campo.etichetta]
                        } 
                        for campo in LayoutCampo.objects.filter(paragrafo__nome='Barra')]
        context['gruppi'] = gruppi
        context['campi_barra'] = campi_barra
        # I campi della barra vanno resi editabili?? Dove??
        
        
        
        if self.request.method == 'POST':
            print('POST!')
            rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])
            form = RifugioForm(self.request.POST, pagina=self.kwargs['pagina'], instance=rifugio)
            # Da' errore in caso di form invalido
            
            if form.is_valid():
                print('VALID!')
                form.save()
            #return HttpResponseRedirect(reverse('polls:results', args=[question.id] ))
            #return HttpResponseRedirect('/rifugi/{}/{}'.format(self.kwargs['pk'], self.kwargs['pagina']))
                
        else:
            rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])
            form = RifugioForm(instance=rifugio, pagina=self.kwargs['pagina'])
       
        return context
 
 
 

        
        
        
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
    
    
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
        
class ImmaginiView(generic.DetailView):
    model = Rifugio
    template_name = 'infomont_app/upload_immagini.html'
    
    def get_context_data(self, **kwargs):
        """ Ritorna il contesto della pagina """
        context = super(ImmaginiView, self).get_context_data(**kwargs)
        context['title'] = "Lista Rifugi"
        context['home'] = 'lista'
        return context





####### TEMPORARY BAD STUFF (remove when no more reference needed) ###################
       
class RRifugioFormView(generic.UpdateView):
    
    model = Rifugio
    #success_url = '/rifugi/{}/{}'.format(self.kwargs['pk'], self.kwargs['pagina'])
    template_name = 'infomont_app/dati_rifugio_form.html'
    
    def get_initial(self):
        initial_data = super(RifugioFormView, self).get_initial()
        obj = self.get_object()
        return initial_data 
        
    def get_object(self, queryset=None):
        rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])   
        return rifugio
        
    def get_form(self):
        rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])
        return RifugioForm(pagina = self.kwargs['pagina'], instance=rifugio)
        
    
    def get_success_url(self):
        return '/rifugi/{}/{}'.format(self.kwargs['pk'], self.kwargs['pagina'])
    
    
    def get_context_data(self, **kwargs):
        """ Ritorna il contesto della pagina """
        
        context = super(RifugioFormView, self).get_context_data(**kwargs)
        obj = self.get_object()
        
        context['url_pagina'] = self.kwargs['pagina']
        context['nome_pagina'] = " ".join([a for a in re.findall('[A-Z][^A-Z]*', self.kwargs['pagina'])])
        context['title'] = "Edit '{}'".format(context['nome_pagina'], context['rifugio'])
        
        gruppi = [ {'nome': gruppo.nome, 'pagine': Pagina.objects.filter(gruppo__nome=gruppo.nome) } for gruppo in Gruppo.objects.all() if gruppo.nome != "Barra"]
        campi_barra = [ {
                            'nome': campo.nome,
                            'valore': Rifugio.objects.filter(nome = context['rifugio'].nome)[0].__dict__[campo.etichetta]
                        } 
                        for campo in LayoutCampo.objects.filter(paragrafo__nome='Barra')]
        context['gruppi'] = gruppi
        context['campi_barra'] = campi_barra
        # I campi della barra vanno resi editabili?? Dove??
        
        
        
        #if self.request.method == 'POST':
        #    print('POST!')
        #    rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])
        #    form = RifugioForm(self.request.POST, pagina=self.kwargs['pagina'], instance=rifugio)
            #print(form)
            
        #    if form.is_valid():
        #        print('VALID!')
        #        form.save()
                #return HttpResponseRedirect(reverse('polls:results', args=[question.id] ))
        #        return HttpResponseRedirect('/rifugi/{}/{}'.format(self.kwargs['pk'], self.kwargs['pagina']))
                
        #else:
        #    rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])
        #    form = self.get_form()#RifugioForm(instance=rifugio, pagina=context['nome_pagina'])
       
        return context
        
    def form_valid(self, form):
        print('VALID!')
        rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])
        form = RifugioForm(self.request.POST, pagina=self.kwargs['pagina'], instance=rifugio)
        form.save()
        #return super(RifugioFormview, self).form_valid(form)    
        return HttpResponseRedirect('/rifugi/{}/{}'.format(self.kwargs['pk'], self.kwargs['pagina']))
        
        
        
        #if self.request.method == 'POST':
       # 
       #     print('POST!')
       #     rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])
       #     form = RifugioForm(self.request.POST, instance=rifugio)
       #     
       #    if form.is_valid():
       #         print('VALID!')
       #        form.save()
       #         HttpResponseRedirect('/rifugi/{}/{}'.format(self.kwargs['pk'], self.kwargs['pagina']))
       #         
       # else:
       #     rifugio = Rifugio.objects.get(pk=self.kwargs['pk'])
       #     form = RifugioForm(instance=rifugio)

        #pagina_url = self.kwargs['pagina']
        #nome_pagina = " ".join([a for a in re.findall('[A-Z][^A-Z]*', pagina_url)])
        
        #context['form'] = form.as_table()
        #context['title'] = "Edit - {}".format(nome_pagina, context['rifugio'])
        
        #return context       
        
        
        
        
