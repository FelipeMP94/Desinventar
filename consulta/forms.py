from django import forms 


class formulario_alimentacao(forms.Form):
    tipo = forms.CharField(label='Tipo desastre',
                           required=True,
                           max_length=100)
    
    data = forms.CharField(label='Data',
                           required=True,
                           max_length=100) 
    
    localizacao = forms.CharField(label='Localizacao',
                                  required=True,
                                  max_length=100) 
    
    escola = forms.CharField(label='Escola',
                             required=True,
                             max_length=100) 