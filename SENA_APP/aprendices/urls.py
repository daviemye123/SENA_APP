from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.aprendices_list, name='aprendices_list'),
    path('aprendices/<int:id>/', views.details, name='details'),
]