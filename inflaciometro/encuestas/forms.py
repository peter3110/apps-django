from django import forms

from .models import datosUsuarioAnonimo
# our new form
class datosUsuarioAnonimoForm(forms.ModelForm):
    ciudad = forms.CharField(max_length=50, label="Ciudad")
    edad = forms.IntegerField(label="Edad")
    expectativaDeInflacion = forms.FloatField(label="Expectativa de inflacion")
    gastoTransporte = forms.IntegerField(label="Gasto en Transporte")
    gastoEducacion = forms.IntegerField(label="Gasto en Educacion")
    gastoVivienda = forms.IntegerField(label="Gasto en Vivienda")
    gastoSalud = forms.IntegerField(label="Gasto en Salud")

    class Meta:
        model = datosUsuarioAnonimo
        fields = '__all__'