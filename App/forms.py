from django import forms

class EmprendimientoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    cuit = forms.IntegerField()
    rubro = forms.CharField(max_length=20)


class EmpleadosFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    DNI = forms.IntegerField()

class ProveedoresFormulario(forms.Form):

    razonsocial = forms.CharField(max_length=30)
    productos = forms.CharField(max_length=30)
    telefono = forms.IntegerField()

class ClientesFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
