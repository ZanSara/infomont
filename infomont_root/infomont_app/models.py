import datetime, re

from django.db import models



class Rifugio(models.Model):
    """ 
        Tabella contenente tutti i dati di ogni rifugio
    """
    
    # Costanti
    EMPTY_CHARFIELD = "<Vuoto>"
    
    
    # Choice Sets
    TIPO_RIFUGIO = (
        ('Custodito', 'Custodito'),
        ('Bivacco', 'Bivacco'),
        ('Stagionale', 'Stagionale'),
    )
    CAT_CAI = (
        ('E', 'Escursionistico'),
        ('A', 'Aplinistico'),
    )
    TIPO_REG = (
        ('E', 'Escursionistico'),
        ('A', 'Aplinistico'),
    )
    
    
    # Campi da mostrare nella barra in alto
    nome            = models.CharField("Nome", max_length=200, default=EMPTY_CHARFIELD)
    localita        = models.CharField("Località", max_length=800, default=EMPTY_CHARFIELD) # Doppio in Dati Geografici
    sezione         = models.CharField("Sezione", max_length=200, default=EMPTY_CHARFIELD)
    regione         = models.CharField("Regione", max_length=200, default=EMPTY_CHARFIELD)
    tipo_rifugio    = models.CharField("Tipo Rifugio", max_length=1, choices=TIPO_RIFUGIO, default="Bivacco")
    #proprieta = ?
    categoria_cai   = models.CharField("Categoria CAI", max_length=1, choices=CAT_CAI, default="E")
    data_inserimento    = models.DateTimeField(("Data Inserimento"))
    data_aggiornamento  = models.DateTimeField(("Data Aggiornamento"))
    
    
    
    # Sottotabelle
    
    # Dati Geografici - Posizione
    #localita    = models.CharField("Località", max_length=200) # Doppio in Rifugio
    comune      = models.CharField("Comune", max_length=200,                    default=EMPTY_CHARFIELD)
    provincia   = models.CharField("Provincia", max_length=200,                 default=EMPTY_CHARFIELD) 
    #regione     = models.CharField("Regione", max_length=200) # Doppio in Rifugio
    competenza = models.CharField("Ente Sovracomunale di Competenza", max_length=200, default=EMPTY_CHARFIELD) 
    gruppo      = models.CharField("Gruppo Montuoso", max_length=200,           default=EMPTY_CHARFIELD) 
    valle       = models.CharField("Valle", max_length=200,                     default=EMPTY_CHARFIELD) 
    quota       = models.IntegerField("Quota",                                  default="0")
    utm_wgs84   = models.DecimalField("UTM WGS84", max_digits=5, decimal_places=5, default="0")  # Cosa sei?
    
    # Dati Geografici - Altro
    zona_tutelata   = models.CharField("Zona Tutelata", max_length=200,         default=EMPTY_CHARFIELD)
    comprensorio    = models.CharField("Comprensorio Sciistico", max_length=200, default=EMPTY_CHARFIELD)
    commissione      = models.CharField("Commissione Regionale", max_length=200, default=EMPTY_CHARFIELD)
    sito            = models.CharField("Sito Web", max_length=200,              default=EMPTY_CHARFIELD)
    
    
    
    
    #anno_costruzione = models.CharField("Regione", max_length=200)
    
    #codice_rifugio      = models.CharField("Codice Rifugio", max_length=200)
    #coordinate_lat      = models.DecimalField("Latitudine", max_digits=9, decimal_places=6)
    #coordinate_long     = models.DecimalField("Longitudine", max_digits=9, decimal_places=6)
    
    
    # Lista di opzioni hardcodate T-T
    # Trova un'alternativa!
    #ANNO_CHOICES = []
    #for r in range(1980, (datetime.datetime.now().year+1)):
    #    ANNO_CHOICES.append((r,r))
    #anno_costruzione = models.IntegerField(('Anno di Costruzione'), max_length=4, choices=ANNO_CHOICES, default=datetime.datetime.now().year)
    
    #tipo_regionale = models.CharField("Tipo Rifugio (secondo legge regionale)", max_length=1, choices=TIPO_REG)
    
    
    def __str__(self):
        return self.nome
        
        
        
        
        
        
        
        
        
        
        

class Gruppo(models.Model):
    """
        Tabella contenente tutti i gruppi.
    """
    nome = models.CharField("Nome Gruppo", max_length=200)
    
    def __str__(self):
        return self.nome
    
        
        
class Pagina(models.Model):
    """
        Tabella contenente tutte le pagine e il loro gruppo di appartenenza.
    """
    nome = models.CharField("Nome Pagina", max_length=200)
    glyph = models.CharField("Glifo Pagina", max_length=50)
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    
           

class Paragrafo(models.Model):
    """
        Tabella contenente tutti i paragrafi e la loro pagina di appartenenza.
    """
    nome = models.CharField("Nome Paragrafo", max_length=200)
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
        
        

        
class LayoutCampo(models.Model):
    """
        Tabella contenente i dati necessari al rendering di ogni campo.
        
        La presenza o meno di tutti i campi dell'oggetto Rifugio come
        righe di questa tabella non e' verificata: assicurarsene al runtime.
    """
    
    nome = models.CharField("Nome Verboso", max_length=200)
    etichetta = models.CharField("Nome Colonna", max_length=200)
    in_alto = models.BooleanField("Presente nella barra riassuntiva", default=False)
    paragrafo = models.ForeignKey(Paragrafo, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nome
