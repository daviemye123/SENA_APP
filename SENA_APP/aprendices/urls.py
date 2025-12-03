from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.aprendices_list, name='aprendices_list'),
    path('<int:id>/', views.details, name='details'),
]