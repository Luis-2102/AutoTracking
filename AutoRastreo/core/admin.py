from django.contrib import admin
from .models import About, Especialidad, Servicio, Portafolio

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('nom','imga1','imga2','imga3', 'created', 'updated')
    search_fields = ('nom','imga1', 'imga2', 'imga3')
    list_filter = ('created', 'updated')

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('Espe', 'created', 'updated')
    search_fields = ('Espe',)
    list_filter = ('created', 'updated')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('svc', 'dcpc', 'icon', 'created', 'updated')
    search_fields = ('svc',)
    list_filter = ('created', 'updated')

@admin.register(Portafolio)
class PortafolioAdmin(admin.ModelAdmin):
    list_display = ('nom', 'detall', 'icon', 'created', 'updated')
    search_fields = ('nom', 'detall', 'icon')
    list_filter = ('created', 'updated')
