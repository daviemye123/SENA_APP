from django.shortcuts import render
from django.template import loader
from .models import curso
from .forms import CursoForm
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy


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


class CursoCreateView(generic.CreateView):
    """Vista para crear un nuevo curso"""
    model = curso
    form_class = CursoForm
    template_name = 'crear_curso.html'
    success_url = reverse_lazy('curso:lista_cursos')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El curso {form.instance.nombre} ha sido creado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class CursoUpdateView(generic.UpdateView):
    """Vista para actualizar un curso existente"""
    model = curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('curso:lista_cursos')
    pk_url_kwarg = 'curso_id'
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El curso {form.instance.nombre} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class CursoDeleteView(generic.DeleteView):
    """Vista para eliminar un curso"""
    model = curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('curso:lista_cursos')
    pk_url_kwarg = 'curso_id'
    
    def delete(self, request, *args, **kwargs):
        curso_obj = self.get_object()
        messages.success(
            request,
            f'El curso {curso_obj.nombre} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)