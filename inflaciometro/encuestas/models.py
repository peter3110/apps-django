from __future__ import unicode_literals
from datetime import date

from django.db import models

#
# python manage.py makemigrations encuestas  || python manage.py migrate
#

# Modelos para la inflacion
class inflacionThomsonReuters(models.Model):
	categoria = models.CharField(max_length=200, default='?')
	porcentaje = models.FloatField(default=0)
	fecha = models.DateField(default=date.today)

	def __str__(self):
		return 'Categoria: ' + self.categoria + ' ' + 'Porcentaje: ' + str(self.porcentaje) + ' ' + 'Fecha: ' + str(self.fecha)

class datosUsuarioAnonimo(models.Model):
	# Datos personales
	ciudad = models.CharField(max_length=50, default='?')
	edad = models.IntegerField(default=0)

	# Expectativas personales
	expectativaDeInflacion = models.FloatField(default=0)

	# Datos sobre gastos
	gastoTransporte = models.IntegerField(default=0)
	gastoEducacion = models.IntegerField(default=0)
	gastoVivienda = models.IntegerField(default=0)
	gastoSalud = models.IntegerField(default=0)

	def __str__(self):
		return 'Ciudad: ' + str(self.ciudad) + ' ' + 'Edad: ' + str(self.edad)
