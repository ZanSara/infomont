from django.contrib import admin

from .models import Rifugio, LayoutCampo, Paragrafo, Pagina, Gruppo

admin.site.register(Rifugio)

admin.site.register(LayoutCampo)
admin.site.register(Paragrafo)
admin.site.register(Pagina)
admin.site.register(Gruppo)
