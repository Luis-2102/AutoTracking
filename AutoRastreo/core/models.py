from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class About(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nombre Vehiculo")
    imga1 = models.ImageField(verbose_name="Imagen1", upload_to='img/', blank=True)
    imga2 = models.ImageField(verbose_name="Imagen2", upload_to='img/', blank=True)
    imga3 = models.ImageField(verbose_name="Imagen2", upload_to='img/', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Acerca de mi'
        verbose_name_plural = 'Acerca de mi'
        ordering = ["-created"]
    def __str__(self):
        return self.nom

class Especialidad(models.Model):
    
    Espe = models.CharField(max_length=100, verbose_name="Sub-Titulo")
    about = models.ManyToManyField(About)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Sub-Titulo'
        verbose_name_plural = 'Sub-Titulos'
        ordering = ["-created"]
    def __str__(self):
        return self.Espe
    
    
class Servicio(models.Model):
   
    svc = models.CharField(max_length=150, verbose_name="Titulo")
    dcpc = models.TextField(verbose_name="Descripcion")
    icon = models.CharField(max_length=50, verbose_name="Icono")
    about = models.ManyToManyField(About)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'
        ordering = ["-created"]
    def __str__(self):
        return self.svc
    
class Portafolio(models.Model):
    
    nom = models.CharField(max_length=100, verbose_name="Titulo Servicios")
    detall = models.TextField(verbose_name="Descripción")
    icon = models.CharField(max_length=100, verbose_name="Icono")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ["-created"]
    def __str__(self):
        return self.nom
    
