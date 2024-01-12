from django.shortcuts import render
from django.http import HttpResponse
from consulta.models import Registros_desastres


# Create your views here.

def registros_desastres(request):

    desastres = Registros_desastres.objects.all()
    return render(request,'consulta/registros_desastres.html',{'ListDesastres':desastres})