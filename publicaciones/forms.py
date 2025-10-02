from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'precio', 'ubicacion', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe tu producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad, barrio…'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
