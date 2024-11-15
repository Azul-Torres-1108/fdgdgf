from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

def inicio_vista(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"misclientes": losclientes})

def registrarCliente(request):
    ID_Cliente = request.POST["txtID_Cliente"]
    Nombre = request.POST["txtNombre"]
    Apellido = request.POST["txtApellido"]
    Correo = request.POST["txtCorreo"]
    Telefono = request.POST["numTelefono"]
    Direccion = request.POST["txtDireccion"]
    Fecha_Registro = request.POST["txtFechaRegistro"]

    Cliente.objects.create(
        ID_Cliente=ID_Cliente,
        Nombre=Nombre,
        Apellido=Apellido,
        Correo=Correo,
        Telefono=Telefono,
        Direccion=Direccion,
        Fecha_Registro=Fecha_Registro,
    )
    return redirect("/")

def borrarCliente(request, ID_Cliente):
    cliente = get_object_or_404(Cliente, ID_Cliente=ID_Cliente)
    cliente.delete()
    return redirect("/")

def seleccionarCliente(request, ID_Cliente):
    cliente = get_object_or_404(Cliente, ID_Cliente=ID_Cliente)
    return render(request, "editarClientes.html", {"cliente": cliente})

def editarCliente(request):
    ID_Cliente = request.POST["txtID_Cliente"]
    Nombre = request.POST["txtNombre"]
    Apellido = request.POST["txtApellido"]
    Correo = request.POST["txtCorreo"]
    Telefono = request.POST["numTelefono"]
    Direccion = request.POST["txtDireccion"]
    Fecha_Registro = request.POST["txtFechaRegistro"]

    cliente = get_object_or_404(Cliente, ID_Cliente=ID_Cliente)

    cliente.Nombre = Nombre
    cliente.Apellido = Apellido
    cliente.Correo = Correo
    cliente.Telefono = Telefono
    cliente.Direccion = Direccion
    cliente.Fecha_Registro = Fecha_Registro
    cliente.save()

    return redirect("/")

