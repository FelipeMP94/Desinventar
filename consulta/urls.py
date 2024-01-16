from django.urls import path
from consulta.views import registros_desastres,alimentando_dados

urlpatterns = [
    path('',registros_desastres,name='registros'),
    path('alimentacao',alimentando_dados,name='alimentacao')
    ]