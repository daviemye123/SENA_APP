from django.db import models

class Programa(models.Model):
    # Campos de identificación y descripción
    nombre = models.CharField(
        max_length=150, 
        unique=True, 
        verbose_name="Nombre del Programa"
    )

    duracion_meses = models.PositiveIntegerField(
        default=6, 
        verbose_name="Duración (meses)"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )
    activo = models.BooleanField(
        default=True, 
        verbose_name="Programa Activo"
    )
    
    class Meta:
        verbose_name = "Programa de Formación"
        verbose_name_plural = "Programas de Formación"
        ordering = ['nombre']

    def __str__(self):
        return f"[{self.codigo_sena or 'N/A'}] {self.nombre}"