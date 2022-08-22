from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    parentesco =  models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField(auto_now_add=False, auto_now=False)
    edad = models.IntegerField()
    

