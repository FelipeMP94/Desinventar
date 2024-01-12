from django import forms 


class login_forms(forms.Form):
    nome_login = forms.CharField(label='Usuario',
                                 required=True,
                                 max_length=100)
    
    senha_login = forms.CharField(label='Senha',
                                 required=True,
                                 max_length=50,
                                 widget=forms.PasswordInput())
    


class cadastro_forms(forms.Form):
    nome_cadastro = forms.CharField(label='Nome de Usuário',
                                 required=True,
                                 max_length=100)
    
    email_cadastro = forms.EmailField(label='Email',
                                      required=True,
                                      max_length=100,
                                      widget=forms.EmailInput())
    
    senha_cadastro1 = forms.CharField(label='Senha',
                                 required=True,
                                 max_length=50,
                                 widget=forms.PasswordInput())
    
    senha_cadastro2 = forms.CharField(label='Confirmar senha',
                                 required=True,
                                 max_length=50,
                                 widget=forms.PasswordInput())