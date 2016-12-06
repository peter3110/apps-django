from django import forms
from .models import datosUsuarioAnonimo

import floppyforms as forms2

class datosUsuarioAnonimoForm(forms.ModelForm):
    ciudad = forms.CharField(max_length=50, label="Ciudad")
    edad = forms.IntegerField(label="Edad")
    expectativaDeInflacion = forms.FloatField(label="Expectativa de inflacion", 
        widget=forms2.RangeInput(attrs={'min':100, 'max':100000, 'step':500}))
    gastoTransporte = forms.IntegerField(label="Gasto en Transporte", 
        widget=forms2.RangeInput(attrs={'min':100, 'max':100000, 'step':500}))
    gastoEducacion = forms.IntegerField(label="Gasto en Educacion", 
        widget=forms2.RangeInput(attrs={'min':100, 'max':100000, 'step':500}))
    gastoVivienda = forms.IntegerField(label="Gasto en Vivienda", 
        widget=forms2.RangeInput(attrs={'min':100, 'max':100000, 'step':500}))
    gastoSalud = forms.IntegerField(label="Gasto en Salud", 
        widget=forms2.RangeInput(attrs={'min':100, 'max':100000, 'step':500}))

    class Meta:
        model = datosUsuarioAnonimo
        fields = '__all__'