from django.contrib import admin
from . models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'queixa', 'pagamento_em_dia')

admin.site.register(Paciente, PacienteAdmin)
