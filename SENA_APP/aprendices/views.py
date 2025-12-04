from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import aprendices 
def aprendices_list(request):
    lista_de_aprendices = aprendices.objects.all()
    template = loader.get_template('all_aprendices.html')
    context = {
        'aprendices': lista_de_aprendices,
        'total_aprendices': lista_de_aprendices.count()
    }
    return HttpResponse(template.render(context, request))
    
def details(request, id):
    un_aprendiz = aprendices.objects.get(id=id)
    template = loader.get_template('aprendiz_detail.html')
    context = {
        'aprendiz': un_aprendiz,
    }
    return HttpResponse(template.render(context, request))
    

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request)) 
