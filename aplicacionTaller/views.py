from django.shortcuts import render
from aplicacionTaller.models import Cliente
# Create your views here.
def clientes(request):
    cliente = Cliente.objects.all()

def renderLogin(request):
    return render(request,"aplicacionTaller/login.html")

def rendermMenu(request):
    return render(request,"aplicacionTaller/menu.html")

def renderCitas(request):
    return render(request,"aplicacionTaller/citas.html")

def servicios_base(request):
    return render(request, "aplicacionTaller/servicios/Base_servicios.html")

def cliente(request):
    return render(request, "aplicacionTaller/servicios/Cliente_servicios.html")

def administrador(request):
    return render(request, "aplicacionTaller/servicios/Administrador_servicios.html")

def mecanico(request):
    return render(request, "aplicacionTaller/servicios/Mecanico_servicios.html")