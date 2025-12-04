from django.contrib import admin
from .models import curso, InstructorCurso, AprendizCurso

# Registrar los modelos pertenecientes a la app 'curso' (solo modelos locales)
admin.site.register(curso)
admin.site.register(InstructorCurso)
admin.site.register(AprendizCurso)
