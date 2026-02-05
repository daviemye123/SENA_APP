from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Programa
from .forms import ProgramaForm
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy


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


class ProgramaCreateView(generic.CreateView):
    """Vista para crear un nuevo programa"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'crear_programa.html'
    success_url = reverse_lazy('programa:programas_list')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El programa {form.instance.nombre} ha sido creado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class ProgramaUpdateView(generic.UpdateView):
    """Vista para actualizar un programa existente"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    success_url = reverse_lazy('programa:programas_list')
    pk_url_kwarg = 'programa_id'
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El programa {form.instance.nombre} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class ProgramaDeleteView(generic.DeleteView):
    """Vista para eliminar un programa"""
    model = Programa
    template_name = 'eliminar_programa.html'
    success_url = reverse_lazy('programa:programas_list')
    pk_url_kwarg = 'programa_id'
    
    def delete(self, request, *args, **kwargs):
        programa_obj = self.get_object()
        messages.success(
            request,
            f'El programa {programa_obj.nombre} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))
