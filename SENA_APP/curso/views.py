from django.shortcuts import render
from django.template import loader
from .models import curso
from django.http import HttpResponse

# Create your views here.
def lista_cursos(request):
    cursos = curso.objects.all()
    template = loader.get_template('list_curso.html')
    
    context = {
        'cursos': cursos,
        'total_cursos': cursos.count(),
    }
    
    return HttpResponse(template.render(context, request))

def detalle_curso(request, curso_id):
    curso_obj = curso.objects.get(id=curso_id)
    aprendices_curso = curso_obj.aprendizcurso_set.all()
    instructores_curso = curso_obj.instructorcurso_set.all()
    template = loader.get_template('detail_curso.html')
    
    context = {
        'curso': curso_obj,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    
    return HttpResponse(template.render(context, request))