from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('crear/', views.CursoCreateView.as_view(), name='crear_curso'),
    path('<int:curso_id>/editar/', views.CursoUpdateView.as_view(), name='editar_curso'),
    path('<int:curso_id>/eliminar/', views.CursoDeleteView.as_view(), name='eliminar_curso'),
    path('<int:curso_id>/', views.detalle_curso, name='detail_curso'),
]
