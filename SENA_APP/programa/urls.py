from django.urls import path
from . import views

app_name = 'programa'

urlpatterns = [
    path('', views.programas_list, name='programas_list'),
    path('crear/', views.ProgramaCreateView.as_view(), name='crear_programa'),
    path('<int:programa_id>/editar/', views.ProgramaUpdateView.as_view(), name='editar_programa'),
    path('<int:programa_id>/eliminar/', views.ProgramaDeleteView.as_view(), name='eliminar_programa'),
    path('<int:id>/', views.programa_detail, name='detalle_programa'),
]