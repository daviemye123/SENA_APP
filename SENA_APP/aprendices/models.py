from django.db import models

class aprendices(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone = models.CharField(max_length=255)
  cedula = models.CharField(max_length=15, default='*********')
  city = models.CharField(max_length=255)
  date_of_birth = models.DateField()
  address = models.CharField(max_length=255)
  programa = models.CharField(max_length=255, blank=True, null=True)
  
  def __str__(self):
    return self.firstname