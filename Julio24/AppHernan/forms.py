from django import forms

class DeporteFormulario(forms.Form):
    deporte = forms.CharField()
    dia = forms.CharField()
    

class BuscaDeporteForm(forms.Form):
    deporte = forms.CharField()


class SociosFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()


class AcreditacionesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()