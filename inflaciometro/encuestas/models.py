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