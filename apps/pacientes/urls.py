from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes, name="pacientes"),
    path('<int:id>', views.paciente_view, name="paciente_view"),
    path('<int:id>/atualizar', views.atualizar_paciente, name="atualizar_paciente"),
]
