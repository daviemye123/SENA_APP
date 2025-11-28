from django.http import HttpResponse
from django.template import loader
from .models import aprendices 
def aprendices_list(request): 
 
    lista_de_aprendices = aprendices.objects.all() 
    template = loader.get_template('all_aprendices.html')
    context = {
        'aprendices': lista_de_aprendices, 
    }
    return HttpResponse(template.render(context, request))
    
def details(request, id):
  
    un_aprendiz = aprendices.objects.get(id=id) 
    template = loader.get_template('details.html')
    context = {
        'aprendices': un_aprendiz, 
    }
    return HttpResponse(template.render(context, request))
    

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request)) 
