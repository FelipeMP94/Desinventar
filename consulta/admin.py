from django.contrib import admin

from consulta.models import Registros_desastres

# Register your models here.

class ListandoDesastres(admin.ModelAdmin):
    list_display = ('id','escola','tipo','publicado')
    list_display_links = ('id','escola')
    list_filter = ('publicado',)




admin.site.register(Registros_desastres,ListandoDesastres)
