from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrarceForm, SecionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto, Carrito
from django.contrib.auth.models import Group
from django.shortcuts import render

def index(request):
    return render(request, 'perfumes/Principal.html')  # Asegúrate de que 'Principal.html' exista

def productos_list(request):
    productos = Producto.objects.all()
    return render(request, 'perfumes/productos_list.html', {'productos': productos})

def Registrarce(request):
    if request.method == 'POST':
        form = RegistrarceForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar usuario al grupo Clientes
            cliente_group = Group.objects.get(name='Clientes')
            cliente_group.user_set.add(user)
            messages.success(request, 'Registro exitoso. Por favor, inicia sesión.')
            return redirect('Secion')
        else:
            print(form.errors)
    else:
        form = RegistrarceForm()
    return render(request, 'perfumes/Registrarce.html', {'form': form})

def Secion(request):
    if request.method == 'POST':
        form = SecionForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            user = authenticate(request, username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin/')
                return redirect('Principal')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = SecionForm()
    return render(request, 'perfumes/Secion.html', {'form': form})

@login_required
def Principal(request):
    productos = Producto.objects.all()
    return render(request, 'perfumes/Principal.html', {'productos': productos})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user, producto=producto)
    if not creado:
        carrito.cantidad += 1
        carrito.save()
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    return render(request, 'perfumes/carrito.html', {'carrito': carrito})

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(Carrito, id=item_id)
    if item.usuario == request.user:
        item.delete()
    return redirect('ver_carrito')

def cerrar_sesion(request):
    logout(request)
    return redirect('Secion')
