from django.contrib import admin
from . models import Paciente, Tarefa, Consulta, Visualizacoes


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'queixa', 'pagamento_em_dia')

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'frequencia')

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('humor', 'paciente', 'data')

# class VisualizacoesAdmin(admin.ModelAdmin):
#     list_display = ('consulta', 'ip')

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Visualizacoes)
