from django.urls import path
from . import views

app_name = 'programa'

urlpatterns = [
    path('', views.programas_list, name='programas_list'),
    path('crear/', views.crear_programa, name='crear_programa'),
    path('<int:id>/', views.programa_detail, name='detalle_programa'),
    path('<int:id>/editar/', views.editar_programa, name='editar_programa'),
]