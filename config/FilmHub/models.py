from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
#-----------------------------------------------------------------------------

class Sala(models.Model):
    id = models.AutoField(primary_key=True)

    numero = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return "Sala: " + str(self.numero)

class Asiento(models.Model):
    id = models.AutoField(primary_key=True)
    reservado = models.BooleanField(default=False)
    fila = models.CharField(max_length=1)
    butaca = models.IntegerField(default=0, blank=True, null=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Fila: " + str(self.fila) + ", Asiento: " + str(self.butaca)

#-----------------------------------------------------------------------------

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)
    portada = models.ImageField(default='default.jpg', upload_to='portadas')
    duracion = models.TimeField(null=True)
    precio_base = models.IntegerField(default=0, blank=True, null=True)
    #funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre) + " (" + str(self.duracion) + ")."

#-----------------------------------------------------------------------------

class Funcion(models.Model):
    id = models.AutoField(primary_key=True)

    horario = models.DateTimeField(null=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, null=True)

    def __str__(self):
        fecha_y_hora = self.horario.strftime("%d/%m/%Y - %H:%M")
        return str(self.pelicula) + " | " + str(self.sala) + " | " + fecha_y_hora

#-----------------------------------------------------------------------------

class Boleto(models.Model):
    id = models.AutoField(primary_key=True)

    asientos = models.ManyToManyField(Asiento, blank=True)
    funcion = models.ForeignKey(Funcion, on_delete=models.SET_NULL, null=True)
    #pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def precio_final(self):
        valor = self.funcion.pelicula.precio_base * len(self.asientos.all())
        self.monto_total = valor
        return "$" + str(valor)

    def __str__(self):
        return str(self.funcion) + " | " + str(self.asientos.all().__str__())

#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------

class Combo_Comida(models.Model):
    id = models.AutoField(primary_key=True)

    comida = models.ForeignKey(Comida, on_delete=models.CASCADE, blank=True, null=True)
    cant_comida = models.IntegerField(default=0, blank=True, null=True)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE, blank=True, null=True)
    cant_bebida = models.IntegerField(default=0, blank=True, null=True)

    

    def __str__(self):
        return str(self.cant_comida) + " " + str(self.comida) + " y " + str(self.cant_bebida) + " " + str(self.bebida)

#-----------------------------------------------------------------------------

class Factura(models.Model):
    boleto = models.ForeignKey(Boleto, on_delete=models.CASCADE)
    combo_comida = models.ForeignKey(Combo_Comida, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    precio_final = models.IntegerField(default=0, blank=True, null=True)

    def precio_total(self):
        valor_boleto = self.boleto.funcion.pelicula.precio_base * len(self.boleto.asientos.all())
        try:
            valor_alimentos = self.combo_comida.comida.precio_unidad * self.combo_comida.cant_comida + self.combo_comida.bebida.precio_unidad * self.combo_comida.cant_bebida
            self.precio_final = valor_boleto + valor_alimentos
            print ("no dio error")
        except:
            self.precio_final = valor_boleto
            print ("dio error")
        self.save()
        

    def __str__(self):
        fechayhora = datetime.datetime.now()
        fecha_y_hora = fechayhora.strftime("%d-%m-%Y %H:%M:%S")
        self.precio_total()
        return "$" + str(self.precio_final)

#-----------------------------------------------------------------------------
