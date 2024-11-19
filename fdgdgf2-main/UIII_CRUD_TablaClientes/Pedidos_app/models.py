from django.db import models

# Create your models here.
class Pedidos(models.Model):
    METODO_PAGO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
    ]
    ID_Pedidos=models.CharField(primary_key=True, max_length=6)
    ID_Cliente=models.CharField(max_length=6)
    Fecha_Pedidos=models.DateField()
    Estado=models.CharField(max_length=100)
    Total = models.DateField()
    Metodo_Pago = models.CharField(max_length=8,choices=METODO_PAGO_CHOICES,default='EFECTIVO')  # Valor predeterminado es 'Efectivo'
    Direccion=models.CharField(max_length=100)

    def __str__(self) :
        return self.Nombre
    def __str__(self):
        return f"Total: {self.get_total_display()} - Método de Pago: {self.get_Metodo_Pago_display()}"
