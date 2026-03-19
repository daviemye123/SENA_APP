from django import forms
from .models import aprendices


class AprendizForm(forms.ModelForm):
    """Formulario basado en el modelo `aprendices`."""

    class Meta:
        model = aprendices
        fields = [
            'firstname',
            'lastname',
            'email',
            'phone',
            'cedula',
            'city',
            'date_of_birth',
            'address',
            'programa',
        ]
        widgets = {
            'firstname':     forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'lastname':      forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email':         forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'phone':         forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'cedula':        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula'}),
            'city':          forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'programa':      forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Programa'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            existing = aprendices.objects.filter(email=email)
            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            if not phone.isdigit():                                        # Solo números
                raise forms.ValidationError("El teléfono debe contener solo números.")
            if len(phone) < 10:                                            # Mínimo 10 dígitos
                raise forms.ValidationError("El teléfono debe tener al menos 10 dígitos.")
        return phone

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if cedula and not cedula.isdigit():                                # Solo números
            raise forms.ValidationError("La cédula debe contener solo números.")
        return cedula