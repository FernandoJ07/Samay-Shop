from django.db import models
import random
import string
import os

# Create your models here.

# Funcion para generar un identificador único y aleatorio alfanumérico de 9 caracteres  
def random_id(lenght=9):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(lenght))

class Producto(models.Model):
    nombre = models.CharField(max_length = 255)
    precio = models.IntegerField()
    categoría = models.ForeignKey("Categoría", on_delete=models.CASCADE, related_name='categoría')
    identificador = models.CharField(primary_key=True, max_length=9, default=random_id, editable=False)
    img = models.ImageField(upload_to='productos', null=True)

    # Eliminar imagen al eliminar el registro del producto 
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.img.path):
            os.remove(self.img.path)
        super(Producto, self).delete(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Categoría(models.Model):
    nombreCategoría = models.CharField(max_length= 50, unique=True)

    def __str__(self):
        return self.nombreCategoría