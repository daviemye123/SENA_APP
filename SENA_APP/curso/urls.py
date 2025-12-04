from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.lista_cursos, name='list_curso'),
    path('<int:curso_id>/', views.detalle_curso, name='detail_curso'),
]
j