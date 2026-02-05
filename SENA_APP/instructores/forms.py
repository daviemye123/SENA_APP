from django import forms
from .models import Instructor, Programa


class InstructorForm(forms.ModelForm):
    """Formulario basado en el modelo `Instructor` (campos acordes al modelo)."""

    class Meta:
        model = Instructor
        fields = [
            'tipo_doc',
            'documento',
            'nombre',
            'especialidad',
            'fecha_nacimiento',
            'ciudad',
            'nivel_formacion',
            'experiencia',
            'activo',
            'fecha_vinculacion',
            'telefono',
            'correo',
            'programa',
        ]
        widgets = {
            'tipo_doc': forms.Select(attrs={'class': 'form-select'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel_formacion': forms.Select(attrs={'class': 'form-select'}),
            'experiencia': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_vinculacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'programa': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        if documento and not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono