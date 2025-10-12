
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FormularioUsuario, FormularioCliente, FormularioMecanico
from django.contrib.auth.hashers import make_password

# Create your views here.


def registro_view(request):
    if request.method == 'POST':
        user_form = FormularioUsuario(request.POST)
        cliente_form = FormularioCliente(request.POST)
        mecanico_form = FormularioMecanico(request.POST)
        tipo_usuario = request.POST.get('tipo_usuario')

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            if tipo_usuario == 'Cliente':
                if cliente_form.is_valid():
                    cliente = cliente_form.save(commit=False)
                    cliente.usuario = user
                    cliente.save()
                    messages.success(request, 'Cliente registrado exitosamente. Por favor, inicie sesión.')
                    return redirect('login')
                else:
                    user.delete() # Eliminar el usuario si el formulario de cliente no es válido
                    messages.error(request, 'Error al registrar el cliente. Por favor, revise los datos.')
            elif tipo_usuario == 'Mecanico':
                if mecanico_form.is_valid():
                    mecanico = mecanico_form.save(commit=False)
                    mecanico.usuario = user
                    mecanico.save()
                    messages.success(request, 'Mecánico registrado exitosamente. Por favor, inicie sesión.')
                    return redirect('login')
                else:
                    user.delete() # Eliminar el usuario si el formulario de mecánico no es válido
                    messages.error(request, 'Error al registrar el mecánico. Por favor, revise los datos.')
            else:
                messages.error(request, 'Tipo de usuario no válido.')
                user.delete()
        else:
            messages.error(request, 'Error en los datos del usuario. Por favor, revise el formulario.')

    else:
        user_form = FormularioUsuario()
        cliente_form = FormularioCliente()
        mecanico_form = FormularioMecanico()

    return render(request, 'aplicacionTaller/registro.html', {
        'user_form': user_form,
        'cliente_form': cliente_form,
        'mecanico_form': mecanico_form,
    })
        

def renderLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')  # Redirige al menú principal
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'aplicacionTaller/login.html')

def rendermMenu(request):
    contexto = {}
    if request.user.is_authenticated:
        if hasattr(request.user, 'perfil_cliente'):
            contexto['rol'] = 'cliente'
            contexto['perfil'] = request.user.perfil_cliente
        elif hasattr(request.user, 'perfil_mecanico'):
            contexto['rol'] = 'mecanico'
            contexto['perfil'] = request.user.perfil_mecanico
        else:
            contexto['rol'] = 'administrador'
    else:
        return redirect('login') # Redirigir a login si no está autenticado
    return render(request,"aplicacionTaller/menu.html", contexto)

@login_required
def renderCitas(request):
    return render(request,"aplicacionTaller/citas.html")

@login_required
def servicios_base(request):
    return render(request, "aplicacionTaller/servicios/Base_servicios.html")

@login_required
def cliente(request):
    return render(request, "aplicacionTaller/servicios/Cliente_servicios.html")

@login_required
def administrador(request):
    return render(request, "aplicacionTaller/servicios/Administrador_servicios.html")

@login_required
def mecanico(request):
    return render(request, "aplicacionTaller/servicios/Mecanico_servicios.html")

