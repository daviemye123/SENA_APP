from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Instructor

def instructores_list(request):
    lista_de_instructores = Instructor.objects.all()
    template = loader.get_template('all_instructor.html')  
    
    context = {
        'instructores': lista_de_instructores,
        'total_instructores': lista_de_instructores.count()  
    }
    return HttpResponse(template.render(context, request))

def instructor_detail(request, id):  
    un_instructor = get_object_or_404(Instructor, id=id)
    template = loader.get_template('instructor_detail.html')
    
    context = {
        'instructor': un_instructor,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))
