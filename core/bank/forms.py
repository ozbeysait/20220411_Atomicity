import imp
from django import forms

class Payment(forms.Form):
    payor = forms.CharField(max_length=50)
    payee = forms.CharField(max_length=50)
    amount = forms.CharField(max_length=50)