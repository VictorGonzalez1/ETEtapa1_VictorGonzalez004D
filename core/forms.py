from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Colaborador

class ColaboradorForm(ModelForm):

    class Meta:
        model = Colaborador
        fields =['rut', 'foto', 'nombre', 'telefono', 'direccion', 'correo', 'pais', 'contraseña']
        labels ={
            'rut': 'Rut', 
            'foto': 'Foto', 
            'nombre': 'Nombre',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'correo': 'Correo',
            'pais': 'Pais',
            'contraseña': 'Contraseña',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese telefono',
                    'id': 'telefono',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese pais', 
                    'id': 'pais'
                }
            ),
            'contraseña': forms.HiddenInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'contraseña'
                }
            ),
            

        }