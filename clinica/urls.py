from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #Paciente
    path('cadastrar_paciente/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('pacientes_cadastrados/', views.pacientes_cadastrados, name='pacientes_cadastrados'),

    #Médico
    path('cadastrar_medico/', views.cadastrar_medico, name='cadastrar_medico'),
    path('medicos_cadastrados/', views.medicos_cadastrados, name='medicos_cadastrados'),

    #Cadastro Especialidade
    path('cadastrar_especialidade/', views.cadastrar_especialidade, name='cadastrar_especialidade'),
    path('especialidades_cadastradas/', views.especialidades_cadastradas, name='especialidades_cadastradas'),

    #Cadastro Exame
    path('cadastrar_exame/', views.cadastrar_exame, name='cadastrar_exame'),
    path('exames_cadastrados/', views.exames_cadastrados, name='exames_cadastrados'),

    #Cadastro Convenio
    path('cadastrar_convenio/', views.cadastrar_convenio, name='cadastrar_convenio'),
    path('convenios_cadastrados/', views.convenios_cadastrados, name='convenios_cadastrados'),

    #Agendamento Exame
    path('agendar_exame', views.agendar_exame, name='agendar_exame'),
    path('exames_agendados/', views.exames_agendados, name='exames_agendados'),

    #Agendamento Consulta
    path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
    path('consultas_agendadas/', views.consultas_agendadas, name='consultas_agendadas'),

    # path('novo/', views.cadastrar, name='cadastro'),
    # path('editar/<int:id>/', views.atualizar_aluno, name='atualizar_aluno'),
]