from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Instructor

def instructores_list(request):
    lista_de_instructores = Instructor.objects.all()
    template = loader.get_template('all_instructor.html')  # Cambiado el nombre del template
    
    context = {
        'instructores': lista_de_instructores,
        'total_instructores': lista_de_instructores.count()  # Agregado para el template
    }
    return HttpResponse(template.render(context, request))

def instructor_detail(request, id):  # Cambiado el nombre de la función
    un_instructor = get_object_or_404(Instructor, id=id)  # Más limpio que try/except
    
    template = loader.get_template('details_instructor.html')  # Cambiado el nombre del template
    
    context = {
        'instructor': un_instructor,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))