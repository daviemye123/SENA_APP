from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .forms import InstructorForm
from django.views import generic
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
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

class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo instructor"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'crear_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar un instructor existente"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    pk_url_kwarg = 'instructor_id'
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un instructor"""
    model = Instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    pk_url_kwarg = 'instructor_id'
    
    def delete(self, request, *args, **kwargs):
        instructor = self.get_object()
        messages.success(
            request,
            f'El instructor {instructor.nombre} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)