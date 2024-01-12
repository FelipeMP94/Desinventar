from django.urls import path
from consulta.views import registros_desastres

urlpatterns = [
    path('',registros_desastres,name='registros'),
    ]