from django.db import models

# Create your models here.

class Paciente(models.Model):
    Id = models.IntegerField()
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField("mm/dd/yyyy",auto_now_add=False, auto_now=False, blank=True)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    actividad_aerobica = models.BooleanField()

def str(self):
    texto = "{0} ({1})"
    return texto.format(self.nombres, self.apellidos)