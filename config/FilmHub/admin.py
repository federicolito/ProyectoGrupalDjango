from django.contrib import admin
from .models import *

class combo_comida_Admin(admin.ModelAdmin):
    exclude = ['monto_total']
    list_display = ['comida', 'cant_comida', 'bebida', 'cant_bebida', 'precio_final']
    list_display_links = ['comida', 'bebida', 'precio_final']

class boleto_Admin(admin.ModelAdmin):
    exclude = ['monto_total']
    list_display = ['pelicula', 'asiento', 'precio_final']


class paquete_Admin(admin.ModelAdmin):
    exclude = ['precio_final']
    list_display = ['__str__', 'precio_total']

# Register your models here.

admin.site.register(Funcion,)
admin.site.register(Asiento,)
admin.site.register(Pelicula,)
admin.site.register(Comida,)
admin.site.register(Bebida,)

admin.site.register(Boleto, boleto_Admin)
admin.site.register(Combo_Comida, combo_comida_Admin)

admin.site.register(Paquete, paquete_Admin)