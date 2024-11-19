from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedidos

def inicio_vista(request):
    lospedidos = Pedidos.objects.all()
    return render(request, "gestionarPedidos.html", {"mispedidos": lospedidos})

def registrarPedidos(request):
    ID_Productos = request.POST["txtID_Productos"]
    ID_Clientes = request.POST["txtID_Clientes"]
    Fecha_Pedidos = request.POST["txtFecha_Pedidos"]
    Estado = request.POST["txtEstado"]
    Total = request.POST["numTotal"]
    Metodo_Pago = request.POST["txtDireccion"]
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

