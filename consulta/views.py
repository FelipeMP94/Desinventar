from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def registros_desastres(request):
    return render(request,'registros_desastres.html')