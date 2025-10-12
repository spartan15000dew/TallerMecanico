from django.contrib import admin
from .models import Cliente, Mecanico

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'telefono')
    search_fields = ('nombre', 'apellido', 'correo', 'telefono')

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'telefono')
    search_fields = ('nombre', 'especialidad', 'telefono')