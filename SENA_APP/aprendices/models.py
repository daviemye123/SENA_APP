from django.db import models

class aprendices(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)       # null=True → campos opcionales
    phone = models.CharField(max_length=255, blank=True, null=True)        # null=True → campos opcionales
    cedula = models.CharField(max_length=15, unique=True)                  # unique=True → no duplicados
    city = models.CharField(max_length=255, blank=True, null=True)         # null=True → campos opcionales
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    programa = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'                          # Retorna nombre + apellido

    def nombre_completo(self):                                              # Método requerido por los tests
        return f'{self.firstname} {self.lastname}'