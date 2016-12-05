from django import forms
from .models import datosUsuarioAnonimo

import floppyforms as forms2

class datosUsuarioAnonimoForm(forms.ModelForm):
    ciudad = forms.CharField(max_length=50, label="Ciudad")
    edad = forms.IntegerField(label="Edad")
    expectativaDeInflacion = forms.FloatField(label="Expectativa de inflacion")
    gastoTransporte = forms.IntegerField(label="Gasto en Transporte")
    gastoEducacion = forms.IntegerField(label="Gasto en Educacion")
    gastoVivienda = forms.IntegerField(label="Gasto en Vivienda")
    #gastoSalud = forms.IntegerField(label="Gasto en Salud")
    #bar = forms2.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'john@example.com'}))
    gastoSalud = forms.IntegerField(label="Gasto en Salud", 
        widget=forms2.RangeInput(attrs={'min':1, 'max':100000, 'step':100}))

    class Meta:
        model = datosUsuarioAnonimo
        fields = '__all__'