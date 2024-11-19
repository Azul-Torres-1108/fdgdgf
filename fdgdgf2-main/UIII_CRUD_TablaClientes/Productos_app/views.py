from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos

def inicio_vista(request):
    losproductos = Productos.objects.all()
    return render(request, "gestionarProductos.html", {"misproductos": losproductos})

def registrarProductos(request):
    ID_Productos = request.POST["txtID_Productos"]
    Nombre = request.POST["txtNombre"]
    Descripcion = request.POST["txtDescripcion"]
    Precio = request.POST["txtPrecio"]
    Cantidad = request.POST["numCantidad"]
    Categoria = request.POST["txtCategoria"]
    Fecha_añadido = request.POST["txtFecha_añadido"]

    Productos.objects.create(
        ID_Productos=ID_Productos,
        Nombre=Nombre,
        Descripcion=Descripcion,
        Precio=Precio,
        Cantidad=Cantidad,
        Categoria=Categoria,
        Fecha_añadido=Fecha_añadido,
    )
    return redirect("/")

def borrarProductos(request, ID_Productos):
    Productos = get_object_or_404(Productos, ID_Productos=ID_Productos)
    Productos.delete()
    return redirect("/")

def seleccionarProductos(request, ID_Productos):
    Productos = get_object_or_404(Productos, ID_Productos=ID_Productos)
    return render(request, "editarProductos.html", {"Productos": Productos})

def editarProductos(request):
    ID_Productos = request.POST["txtID_Productos"]
    Nombre = request.POST["txtNombre"]
    Descripcion = request.POST["txtDescripcion"]
    Precio = request.POST["txtPrecio"]
    Cantidad = request.POST["numCantidad"]
    Categoria = request.POST["txtCategoria"]
    Fecha_añadido = request.POST["txtFecha_añadido"]

    Productos = get_object_or_404(Productos, ID_Productos=ID_Productos)

    Productos.ID_Productos = ID_Productos
    Productos.Nombre = Nombre
    Productos.Descripcion = Descripcion
    Productos.Precio = Precio
    Productos.Cantidad = Cantidad
    Productos.Categoria = Categoria
    Productos.Fecha_añadido = Fecha_añadido
    Productos.save()

    return redirect("/")

