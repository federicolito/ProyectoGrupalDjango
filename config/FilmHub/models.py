from django.db import models

# Create your models here.

class Funcion(models.Model):
    id = models.AutoField(primary_key=True)

    horario = models.CharField(max_length=5)

    def __str__(self):
        return (self.horario)

class Asiento(models.Model):
    id = models.AutoField(primary_key=True)

    fila = models.CharField(max_length=1)
    butaca = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return (self.fila + str(self.butaca))

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)
    duracion = models.IntegerField(default=0, blank=True, null=True)
    precio_base = models.IntegerField(default=0, blank=True, null=True)
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)

    def __str__(self):
        return(self.nombre + " " + "(" + str(self.duracion) + "min.)" + " - " + str(self.funcion))

class Comida(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=25)
    contenido_neto = models.IntegerField(default=0, blank=True, null=True)
    precio_unidad = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return (self.nombre + " (" + str(self.contenido_neto) + "g)" + " - " + "$" + str(self.precio_unidad))

class Bebida(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=25)
    contenido_neto = models.IntegerField(default=0, blank=True, null=True)
    precio_unidad = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return (self.nombre + " (" + str(self.contenido_neto) + "ml)" + " - " + "$" + str(self.precio_unidad))



class Boleto(models.Model):
    asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    monto_total = models.IntegerField(default=0, blank=True, null=True)

    def precio_final(self):
        valor = self.pelicula.precio_base
        self.monto_total = valor
        return valor
        
    monto_total.short_description = 'Monto Total'

    def __str__(self):
        return str(self.pelicula) + ' - Asiento: ' + str(self.asiento)

class Combo_Comida(models.Model):
    id = models.AutoField(primary_key=True)

    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)
    cant_comida = models.IntegerField(default=0, blank=True, null=True)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    cant_bebida = models.IntegerField(default=0, blank=True, null=True)

    monto_total = models.IntegerField(default=0, blank=True, null=True)

    def precio_final(self):
        valor = (self.comida.precio_unidad * self.cant_comida + self.bebida.precio_unidad * self.cant_bebida)
        self.monto_total = valor
        return valor

    def __str__(self):
        return str(self.cant_comida) + " " + str(self.comida) + " y " + str(self.cant_bebida) + " " + str(self.bebida)



class Paquete(models.Model):
    boleto = models.ForeignKey(Boleto, on_delete=models.CASCADE)
    combo_comida = models.ForeignKey(Combo_Comida, on_delete=models.CASCADE)
    precio_final = models.IntegerField(default=0, blank=True, null=True)


    def precio_total(self):
        valor_boleto = self.boleto.precio_final()
        valor_combo = self.combo_comida.precio_final()
        valor = valor_boleto + valor_combo

        self.precio_final = valor
        return valor
    
    