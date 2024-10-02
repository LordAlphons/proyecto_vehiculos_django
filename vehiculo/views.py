from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from tokenize import PseudoExtras
from django.views.generic import TemplateView
from .forms import InputForm, WidgetForm, RegistroUsuarioForm, VehiculoForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from vehiculo.models import Vehiculo

# Create your views here.

from django.views.generic import TemplateView
class IndexPageView(TemplateView):
    template_name = "index.html"

def menuView(request):
 template_name = 'menu.html'
 return render(request, template_name)

def navbar(request):
   
   return render(request, 'navbar.html', {})

def footer(request):
   
   return render(request, 'footer.html', {})

class Persona(object):
    def __init__ (self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido 

def datosform_view(request):
    context = {}
    context['form']= InputForm()
    return render(request, "datosform.html", context)

def widget_view(request):
 context = {}
 form = WidgetForm(request.POST or None)
 context['form'] = form
 return render(request, "widget_home.html", context)

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            # Guardar el nuevo usuario
            user = form.save()
            
            # Obtener el content type del modelo Vehiculo
            content_type = ContentType.objects.get_for_model(Vehiculo)
            
            # Obtener el permiso 'visualizar_catalogo'
            visualizar_catalogo_permiso = Permission.objects.get(
                codename='visualizar_catalogo',
                content_type=content_type
            )
            
            # Asignar el permiso al usuario
            user.user_permissions.add(visualizar_catalogo_permiso)
            
            # Iniciar sesión automáticamente
            login(request, user)
            messages.success(request, "Registrado satisfactoriamente con permisos para visualizar el catálogo.")
            return HttpResponseRedirect('/menu')
        
        messages.error(request, "Registro inválido. Algunos datos ingresados no son correctos.")
    
    else:
        form = RegistroUsuarioForm()

    return render(
        request=request,
        template_name="registration/registro.html",
        context={"register_form": form}
    )

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/menu')
            else:
                messages.error(request,"Invalido username o password.")
        else:
            messages.error(request,"Invalido username o password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/menu')

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def vehiculo_add(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo vehículo en la base de datos
            messages.success(request, "Vehículo agregado exitosamente.")
            return redirect('vehiculo_list')  # Redirige a la lista de vehículos
        else:
            messages.error(request, "Error al agregar el vehículo. Por favor, verifica los datos.")
    else:
        form = VehiculoForm()

    return render(request, 'vehiculo_add.html', {'form': form})

@login_required
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo_list.html', {'vehiculos': vehiculos})