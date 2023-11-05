from django.db import models

# Create your models here.



class Psicologo(models.Model):
    nombre = models.CharField(max_length=100) 
    promedio_calificaciones = models.FloatField()
    cantidad_calificaciones = models.IntegerField()
    suma_calificaciones = models.FloatField()
    def __str__(self):
        return '{}'.format(self.nombre)  


class Calificacion(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)
    puntuacion = models.FloatField()

class Calificacion2(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)
    puntuacion = models.FloatField()
    

class Calificaciones(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)
    puntuacion = models.FloatField()


class Calificacionessonar(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)
    puntuacion = models.FloatField()

class Psicologo245(models.Model):
    nombre = models.CharField(max_length=100) 
    promedio_calificaciones = models.FloatField()
    cantidad_calificaciones = models.IntegerField()
    suma_calificaciones = models.FloatField()
    def __str__(self):
        return '{}'.format(self.nombre)  