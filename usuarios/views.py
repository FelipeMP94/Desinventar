from django.shortcuts import render,redirect
from usuarios.forms import login_forms,cadastro_forms
from django.contrib.auth.models import User
from django.contrib import auth,messages


# Create your views here.
def login(request):
    form = login_forms()
    if request.method == 'POST':
        form = login_forms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha_login'].value()
            
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
            )
        
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request,f'{nome} logado com sucesso')
            return redirect('alimentacao')
        else:
            messages.error(request,'Erro ao logar')
            return redirect('login')


    return render(request,'usuarios/login.html',{'form':form}) 

def cadastro(request):
    form = cadastro_forms()
    if request.method == 'POST':
        form = cadastro_forms(request.POST)

        if form.is_valid():
            if form['senha_cadastro1'].value() != form['senha_cadastro2'].value():
                messages.error(request,'Senhas devem ser iguais')
                return redirect('cadastro')

            nome= form['nome_cadastro'].value()        
            email= form['email_cadastro'].value()  
            senha= form['senha_cadastro1'].value()  

            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já cadastrado')
                return redirect('cadastro')



            usuario = User.objects.create_user(username=nome,
                                               email=email,
                                               password=senha)
            usuario.save()
            messages.success(request,'Novo usuário cadastrado')
            return redirect('login')

    return render(request,'usuarios/cadastro.html',{'form':form})