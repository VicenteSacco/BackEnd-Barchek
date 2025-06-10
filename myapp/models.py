from django.db import models
from django.utils.timezone import now

class Administrador(models.Model):
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    pin = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.correo_electronico

class Barra(models.Model):
    numero_de_barra = models.CharField(max_length=50, unique=True)
    cantidad_bartender = models.IntegerField()
    nombre_de_la_barra = models.CharField(max_length=100)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name='barras')

    def __str__(self):
        return self.nombre_de_la_barra

class Categoría(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Alcohol(models.Model):
    codigo_de_barra = models.CharField(max_length=100, unique=True)
    stock_actual = models.IntegerField()
    cantidad_cc = models.IntegerField()
    marca = models.CharField(max_length=100)
    año = models.IntegerField()
    ia = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoría, on_delete=models.CASCADE, related_name='alcoholes')

    def __str__(self):
        return self.nombre

class CarouselItem(models.Model):
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, related_name='carousel_items')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class ListaDeAlcohol(models.Model):
    nombre = models.CharField(max_length=100)
    barra = models.ForeignKey(Barra, on_delete=models.CASCADE, related_name='listas_de_alcohol')
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name='listas_de_alcohol')
    alcoholes = models.ManyToManyField(Alcohol, related_name='listas_de_alcohol')

    def __str__(self):
        return self.nombre

class Reporte(models.Model):
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name='reportes')
    fecha = models.DateTimeField(default=now)

    def __str__(self):
        return f"Reporte {self.id} - {self.fecha}"
