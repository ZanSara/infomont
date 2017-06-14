import re, collections

from django import forms

from .models import Rifugio, LayoutCampo, Paragrafo

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
    

class RifugioForm(forms.ModelForm):

    def __init__(self, pagina, *args, **kwargs):
        super(RifugioForm, self).__init__(*args, **kwargs)       
        
        print(pagina)
        nomepagina = " ".join([a for a in re.findall('[A-Z][^A-Z]*', pagina)])
        
        paragrafi = [ [campo.etichetta for campo in LayoutCampo.objects.filter(paragrafo__nome=paragrafo.nome)]
                       for paragrafo in Paragrafo.objects.filter(pagina__nome=nomepagina)]
        campi = sum(paragrafi, [])
        
        nuovi_campi = collections.OrderedDict()
        for fieldname, fieldvalue in self.fields.items():
            if fieldname in campi:
                nuovi_campi[fieldname] = fieldvalue
        
        self.fields = nuovi_campi
        

    class Meta:
        model = Rifugio
        fields = '__all__'
