from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes, name="pacientes"),
    path('<int:id>', views.paciente_view, name="paciente_view"),
    path('<int:id>/atualizar', views.atualizar_paciente, name="atualizar_paciente"),
    path('excluir-consulta/<int:id>', views.excluir_consulta, name="excluir_consulta"),
    path('consulta-publica/<int:id>', views.consulta_publica, name="consulta_publica"),
]
