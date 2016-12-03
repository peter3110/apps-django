from django import forms

from .models import datosUsuarioAnonimo
# our new form
class datosUsuarioAnonimoForm(forms.ModelForm):
    ciudad = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    expectativaDeInflacion = forms.FloatField()
    gastoTransporte = forms.IntegerField()
    gastoEducacion = forms.IntegerField()
    gastoVivienda = forms.IntegerField()
    gastoSalud = forms.IntegerField()

    class Meta:
        model = datosUsuarioAnonimo
        fields = '__all__'