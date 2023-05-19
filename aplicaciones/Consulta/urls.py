from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarPaciente/', views.registrarPaciente),
    path('edicionPaciente/<id>', views.edicionPaciente),
    path('editarPaciente/', views.editarPaciente),
    path('eliminarPaciente/<id>', views.eliminarPaciente)
]