from itertools import product
from django.shortcuts import render, HttpResponse
from App.models import *
from App.forms import *

# Create your views here.
def inicio(request):

    return render(request, "App/inicio.html")


def emprendimiento(request):

    if request.method == 'POST':

        miFormulario = EmprendimientoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            empleado = Emprendimiento(nombre=info['nombre'], cuit=info['cuit'], rubro=info['rubro'])
            empleado.save()

            return render(request, "App/inicio.html")
    else:
        miFormulario = EmprendimientoFormulario()

    return render(request, "App/emprendimiento.html", {"miFormulario":miFormulario})



def empleados(request):

    if request.method == 'POST':

        miFormulario = EmpleadosFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            empleado = Empleados(nombre=info['nombre'], apellido=info['apellido'], DNI=info['DNI'])
            empleado.save()

            return render(request, "App/inicio.html")
    else:
        miFormulario = EmpleadosFormulario()

    return render(request, "App/empleados.html", {"miFormulario":miFormulario})


def proveedores(request):

    if request.method == 'POST':

        miFormulario =ProveedoresFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            empleado = Proveedores(razonsocial=info['razonsocial'], productos=info['productos'], telefono=info['telefono'])
            empleado.save()

            return render(request, "App/inicio.html")
    else:
        miFormulario = ProveedoresFormulario()

    return render(request, "App/proveedores.html", {"miFormulario":miFormulario})



def clientes(request):

    if request.method == 'POST':

        miFormulario = ClientesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            empleado = Clientes(nombre=info['nombre'], telefono=info['telefono'])
            empleado.save()

            return render(request, "App/inicio.html")
    else:
        miFormulario = ClientesFormulario()

    return render(request, "App/clientes.html", {"miFormulario":miFormulario})


def buscar(request):

    if request.GET['productos']:

        productos = request.GET['productos']
        print(productos)
    
        proveedores = Proveedores.objects.filter(productos__icontains=productos)
        print(proveedores)

        return render(request, "App/inicio.html", {"proveedores":proveedores.values,"prd":productos})
    else:

        respuesta = "Sin datos"

    return render(request, "App/inicio.html", {"prd":respuesta})

