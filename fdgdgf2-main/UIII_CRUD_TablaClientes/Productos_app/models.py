from django.db import models

# Create your models here.
class Productos(models.Model):
    ID_Productos=models.CharField(primary_key=True, max_length=6)
    Nombre=models.CharField(max_length=100)
    Descripcion=models.CharField(max_length=100)
    Precio=models.CharField(max_length=100)
    Cantidad=models.CharField(max_length=15)
    Categoria=models.CharField(max_length=100)
    Fecha_añadido=models.DateField()

    def __str__(self) :
        return self.Nombre