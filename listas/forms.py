from django import forms
from django.forms import ModelForm
from .models import Tarea_ind


class Tarea_form(forms.ModelForm):
    
    class Meta:
        model= Tarea_ind
        fields= '__all__'


class Raw_tarea_form(forms.Form):
    titulo=forms.CharField()
    status=forms.BooleanField()
    #creado=forms.DateTimeField()
    descripcion=forms.CharField()