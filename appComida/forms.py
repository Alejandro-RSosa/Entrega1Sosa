from django import forms


class Form_comida(forms.Form):
    nombre = forms.CharField(max_length=20)
    desc = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)