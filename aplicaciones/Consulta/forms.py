from django import forms

from aplicaciones.Consulta.models import Paciente

class PacienteForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        exclude = []