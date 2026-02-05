from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    path('', views.instructores_list, name='instructores_list'),
    path('crear/', views.InstructorCreateView.as_view(), name='crear_instructor'),
    path('<int:instructor_id>/editar/', views.InstructorUpdateView.as_view(), name='editar_instructor'),
    path('<int:instructor_id>/eliminar/', views.InstructorDeleteView.as_view(), name='eliminar_instructor'),
    path('<int:id>/', views.instructor_detail, name='instructor_detail'),
]