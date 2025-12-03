from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Programa

def programas_list(request):
    programas = Programa.objects.all()
    template = loader.get_template('all_programa.html')
    context = {
        'programas': programas,
        'total_programas': programas.count()
    }
    return HttpResponse(template.render(context, request))

def programa_detail(request, id):
    programa = get_object_or_404(Programa, id=id)
    template = loader.get_template('detail_programa.html')
    context = {
        'programa': programa,
    }
    return HttpResponse(template.render(context, request))

def crear_programa(request):
    return HttpResponse('Crear programa - no implementado aún', status=200)

def editar_programa(request, id):
    return HttpResponse(f'Editar programa {id} - no implementado aún', status=200)

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))
