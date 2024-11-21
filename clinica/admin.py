from django.contrib import admin
from .models import Paciente, Medico, ConsultaAgendada, ExameAgendado, ExameClinica, EspecialidadeClinica, Convenio

# admin.site.register(Paciente)
admin.site.register(ExameClinica)
# admin.site.register(Ficha)
# Register your models here.
