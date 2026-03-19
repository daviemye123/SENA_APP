from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.aprendices_list, name='aprendices_list'),
    path('crear/', views.AprendizCreateView.as_view(), name='aprendiz_create'),          # era 'crear_aprendiz'
    path('aprendiz/<int:id>/', views.details, name='details'),                           # era '<int:id>/'
    path('<int:pk>/editar/', views.AprendizUpdateView.as_view(), name='aprendiz_update'),# era 'editar_aprendiz'
    path('<int:pk>/eliminar/', views.AprendizDeleteView.as_view(), name='aprendiz_delete'),# era 'eliminar_aprendiz'
]