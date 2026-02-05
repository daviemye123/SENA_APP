from django import forms
from .models import Programa


class ProgramaForm(forms.ModelForm):
    """Formulario basado en el modelo `Programa`."""

    class Meta:
        model = Programa
        fields = [
            'codigo',
            'nombre',
            'nivel_formacion',
            'modalidad',
            'duracion_meses',
            'duracion_horas',
            'descripcion',
            'competencias',
            'perfil_egreso',
            'requisitos_ingreso',
            'centro_formacion',
            'regional',
            'estado',
            'fecha_creacion',
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código del Programa'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Programa'}),
            'nivel_formacion': forms.Select(attrs={'class': 'form-select'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'duracion_meses': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'competencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'perfil_egreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'requisitos_ingreso': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'centro_formacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Centro de Formación'}),
            'regional': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Regional'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if codigo:
            # Verificar si el código ya existe (excluyendo el objeto actual en caso de edición)
            existing = Programa.objects.filter(codigo=codigo)
            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise forms.ValidationError("Este código de programa ya está registrado.")
        return codigo
