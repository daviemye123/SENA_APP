from django.db import models

# Definiciones de Choices
DOC_CHOICES = [
    ('C.C', 'Cédula de Ciudadanía'),
    ('C.E', 'Cédula de Extranjería'),
    ('P.A', 'Pasaporte'),
]

NIVEL_CHOICES = [
    ('TEC', 'Técnico'),
    ('TGL', 'Tecnólogo'),
    ('PRE', 'Pregrado'),
    ('ESP', 'Especialización'),
    ('MAE', 'Maestría'),
    ('DOC', 'Doctorado'),
    ('N.A', 'No Aplica'),
]

# Modelo de Ejemplo: Programa (si está en el mismo archivo o app)
class Programa(models.Model):
    nombre = models.CharField(max_length=150, unique=True, verbose_name="Nombre del Programa")
    
    def __str__(self):
        return self.nombre
        
# --- Modelo Instructor ---
class Instructor(models.Model):
    tipo_doc = models.CharField(max_length=3, choices=DOC_CHOICES, default='C.C', verbose_name="Tipo de Documento")
    documento = models.CharField(max_length=20, unique=True, verbose_name="Número de Documento")
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad o Área")
    
    
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad de Residencia")
    nivel_formacion = models.CharField(max_length=3, choices=NIVEL_CHOICES, default='N.A', verbose_name="Nivel de Formación")
    experiencia = models.PositiveIntegerField(default=0, verbose_name="Años de Experiencia")
    activo = models.BooleanField(default=True, verbose_name="Instructor Activo")
    fecha_vinculacion = models.DateField(verbose_name="Fecha de Vinculación")
    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    correo = models.EmailField(unique=True, blank=True, null=True, verbose_name="Correo Electrónico")
    
    # MEJORA: Relación con la tabla Programa
    programa = models.ForeignKey(
        'Programa', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        verbose_name="Programa Asignado"
    )

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"