from django.db import models

# Create your models here.

class Registros_desastres(models.Model):
    tipo = models.CharField(max_length= 100,null=False,blank=False)
    data = models.CharField(max_length= 100,null=False,blank=False)
    localizacao = models.CharField(max_length= 100,null=False,blank=False)
    escola = models.CharField(max_length= 100,null=False,blank=False)


