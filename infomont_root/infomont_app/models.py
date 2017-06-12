from django.db import models


class Rifugio(models.Model):
    nome        = models.CharField(max_length=200)
    localita    = models.CharField(max_length=800)
    sezione     = models.CharField(max_length=200)
    regione     = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

