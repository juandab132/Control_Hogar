# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Usuario, Camera, Light
#from .forms import ClienteForm, ResultadosForm  # Necesitarás crear formularios para la creación y actualización

# Vista para listar todos los clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def lista_usuarios(request):
    Usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'Usuarios': Usuarios})
def CamMenu(request):
    camera = Camera.objects.all()
    return render(request, 'CamMenu.html', {'Cameras': camera})
def mainMenu(request):
    return render(request, 'MainMenu.html')
def logIn(request):
    return render(request, 'LogInPage.html')
def lightsMenu(request):
    light = Light.objects.all()
    return render(request, 'LightsMenu.html', {'Lights': light})
def toggle_boolean(request):
    # Get the instance of the model you want to update
    instance = Light.objects.get(pk=request.GET.get('pk'))
    
    # Toggle the boolean attribute
    instance.status = not instance.status
    instance.save()
    
    # Return a JSON response with the new state of the boolean attribute
    return JsonResponse({'new_state': instance.boolean_attribute})