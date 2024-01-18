from django.shortcuts import render,redirect
from django.http import HttpResponse
from consulta.models import Registros_desastres
from consulta.forms import formulario_alimentacao
from consulta.models import Registros_desastres
from django.contrib import auth,messages



# Create your views here.

def registros_desastres(request):

    desastres = Registros_desastres.objects.filter(publicado=True)
    return render(request,'consulta/registros_desastres.html',{'ListDesastres':desastres})



def alimentando_dados(request):
    if request.user.is_authenticated:
        form = formulario_alimentacao()
        if request.method == 'POST':
            form = formulario_alimentacao(request.POST)
            if form.is_valid():
                #Validações aqui 

                tipo = form['tipo'].value()
                data = form['data'].value()
                localizacao = form['localizacao'].value()
                escola = form['escola'].value()

                novo_registro = Registros_desastres(tipo=tipo,data=data,localizacao=localizacao,escola=escola)
                novo_registro.save()
                messages.success(request,'Registro enviado')

                return redirect('alimentacao')



        return render(request,'alimentacao/formulario_alimentacao.html',{'form':form})