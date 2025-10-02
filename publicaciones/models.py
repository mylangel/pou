from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo
