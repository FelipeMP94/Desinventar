from django.contrib import admin

from consulta.models import Registros_desastres

# Register your models here.

class ListandoDesastres(admin.ModelAdmin):
    list_display = ('id','escola','tipo')
    list_display_links = ('id','escola')


admin.site.register(Registros_desastres,ListandoDesastres)