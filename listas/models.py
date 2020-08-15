from django.db import models

# Create your models here.
class Tarea_ind(models.Model):
    titulo = models.CharField(max_length=200, default=" ")
    status = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True, )
    detalles =models.TextField(max_length=300, default=" g")

    def __str__(self):
        return self.titulo