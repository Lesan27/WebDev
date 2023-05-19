from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from aplicaciones.Consulta.forms import PacienteForm
from .models import Paciente
# Create your views here.

def home (request):
    pacientesListados=Paciente.objects.all()
    return render(request, "gestionPacientes.html", {"pacientes":pacientesListados, "form":PacienteForm()})

def registrarPaciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            print('guarde')
            form.save()
            return HttpResponseRedirect("/")
        print("no guarde")
        return render(request, "gestionPacientes.html", {"pacientes":Paciente.objects.all(), "form":form})
    form = PacienteForm()
    return HttpResponseRedirect("/")

    #paciente=Paciente.objects.create(id=id, nombres=nombres,apellidos=apellidos,fecha_nacimiento=fecha_nacimiento, sexo=sexo, altura=altura, peso_inicial=peso_inicial, actividad_aerobica=actividad_aerobica)

    #return redirect('/')

def edicionPaciente (request, id):
    paciente = Paciente.objects.get(id=id)
    return render(request, "edicionPaciente.html", {"paciente": paciente})


def editarPaciente (request):
    id=request.POST['txtCodigo']
    nombres=request.POST['txtNombres']
    apellidos=request.POST['txtApellidos']
    fecha_nacimiento=request.POST['numFecha']
    sexo=request.POST['txtSexo']
    altura=request.POST['numAltura']
    peso_inicial=request.POST['numPeso']
    actividad_aerobica=request.POST['txtActv']

    paciente = Paciente.objects.get(id=id)
    paciente.nombres = nombres
    paciente.apellidos = apellidos
    paciente.fecha_nacimiento = fecha_nacimiento
    paciente.sexo = sexo
    paciente.altura = altura
    paciente.peso_inicial = peso_inicial
    paciente.actividad_aerobica = actividad_aerobica
    paciente.save()
    return redirect('/')

def eliminarPaciente(request, id):

    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    return redirect('/')

def redirectPaciente(request):
    return redirect('/admin')