from django.contrib import admin
from . models import Paciente, Tarefa, Consulta


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'queixa', 'pagamento_em_dia')

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'frequencia')

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('humor', 'paciente', 'data')

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Consulta, ConsultaAdmin)
