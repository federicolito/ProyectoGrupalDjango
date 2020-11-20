from django.contrib import admin
from .models import *

#-----------------------------------------------------------------------------

class sala_Admin(admin.ModelAdmin):
    pass

class asiento_Admin(admin.ModelAdmin):
    list_display = ['fila', 'butaca']
    list_display_links = ['fila', 'butaca']
    fieldsets = (
        ('Asiento', {
            'fields':('fila', 'butaca')
        }),
        ('Sala', {
            'fields':('sala',)
        })
    )

class pelicula_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion']
    list_display_links = ['nombre', 'duracion']

class funcion_Admin(admin.ModelAdmin):
    list_display = ['pelicula', 'sala', 'horario']
    list_display_links = ['pelicula', 'sala', 'horario']
    fieldsets = (
        ('Película', {
            'fields':('pelicula',)
        }),
        ('Sala', {
            'fields':('sala',)
        }),
        ('Horario', {
            'fields':('horario',)
        })
    )



class boleto_Admin(admin.ModelAdmin):
    exclude = ['monto_total']
    list_display = ['funcion', 'asiento', 'precio_final']
    list_display_links = ['funcion', 'asiento', 'precio_final']

#-----------------------------------------------------------------------------

class comida_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'contenido_neto', 'precio_unidad']
    list_display_links = ['nombre', 'contenido_neto', 'precio_unidad']

class bebida_Admin(admin.ModelAdmin):
    list_display = ['nombre', 'contenido_neto', 'precio_unidad']
    list_display_links = ['nombre', 'contenido_neto', 'precio_unidad']



class combo_comida_Admin(admin.ModelAdmin):
    exclude = ['monto_total']
    list_display = ['comida', 'cant_comida', 'bebida', 'cant_bebida', 'precio_final']
    list_display_links = ['comida', 'bebida', 'precio_final']

#-----------------------------------------------------------------------------

class factura_Admin(admin.ModelAdmin):
    exclude = ['precio_final']
    list_display = ['boleto', 'combo_comida', '__str__']
    list_display_links = ['boleto', 'combo_comida', '__str__']

#-----------------------------------------------------------------------------

# Register your models here.

#-----------------------------------------------------------------------------

admin.site.register(Sala, sala_Admin)
admin.site.register(Asiento, asiento_Admin)
admin.site.register(Pelicula, pelicula_Admin)
admin.site.register(Funcion, funcion_Admin)

admin.site.register(Boleto, boleto_Admin)

#-----------------------------------------------------------------------------

admin.site.register(Comida, comida_Admin)
admin.site.register(Bebida, bebida_Admin)

admin.site.register(Combo_Comida, combo_comida_Admin)

#-----------------------------------------------------------------------------

admin.site.register(Factura, factura_Admin)

#-----------------------------------------------------------------------------