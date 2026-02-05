from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import aprendices
from .forms import AprendizForm
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy


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


class AprendizCreateView(generic.CreateView):
    """Vista para crear un nuevo aprendiz"""
    model = aprendices
    form_class = AprendizForm
    template_name = 'crear_aprendiz.html'
    success_url = reverse_lazy('aprendices:aprendices_list')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El aprendiz {form.instance.firstname} {form.instance.lastname} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class AprendizUpdateView(generic.UpdateView):
    """Vista para actualizar un aprendiz existente"""
    model = aprendices
    form_class = AprendizForm
    template_name = 'editar_aprendiz.html'
    success_url = reverse_lazy('aprendices:aprendices_list')
    pk_url_kwarg = 'aprendiz_id'
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El aprendiz {form.instance.firstname} {form.instance.lastname} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class AprendizDeleteView(generic.DeleteView):
    """Vista para eliminar un aprendiz"""
    model = aprendices
    template_name = 'eliminar_aprendiz.html'
    success_url = reverse_lazy('aprendices:aprendices_list')
    pk_url_kwarg = 'aprendiz_id'
    
    def delete(self, request, *args, **kwargs):
        aprendiz_obj = self.get_object()
        messages.success(
            request,
            f'El aprendiz {aprendiz_obj.firstname} {aprendiz_obj.lastname} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs) 
