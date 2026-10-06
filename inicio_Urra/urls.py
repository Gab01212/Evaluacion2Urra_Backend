from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tema/<int:tema_id>/', views.tema_detalle, name='tema_detalle'),
]
