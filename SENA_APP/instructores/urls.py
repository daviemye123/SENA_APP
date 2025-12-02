from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    path('', views.instructores_list, name='instructores_list'),
    path('<int:id>/', views.instructor_detail, name='instructor_detail'),  # Nombre de función actualizado
    path('main/', views.main, name='main'),  # Si necesitas la vista main
]