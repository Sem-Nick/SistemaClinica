from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Medico, ExameAgendado, ConsultaAgendada, ExameClinica, EspecialidadeClinica, Convenio
from .forms import PacienteForm, MedicoForm, ExameAgendadoForm, ConsultaAgendadaForm, ExameClinicaForm, EspecialidadeClinicaForm, ConvenioForm

def index(request):
    return render(request, 'pacientes/index.html')


#Paciente
def pacientes_cadastrados(request):
    pacientes = Paciente.objects.all()
    return render(request, 'recepcionistas/pacientes_cadastrados.html', {'pacientes': pacientes})

def cadastrar_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pacientes_cadastrados')
    else:
        form = PacienteForm()
    return render(request, 'recepcionistas/cadastrar_paciente.html', {'form': form})


#Cadastro Especialidade
def especialidades_cadastradas(request):
    especialidades = EspecialidadeClinica.objects.all()
    return render(request, 'recepcionistas/especialidades_cadastradas.html', {'especialidades': especialidades})

def cadastrar_especialidade(request):
    if request.method == "POST":
        form = EspecialidadeClinicaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('especialidades_cadastradas')
    else:
        form = EspecialidadeClinicaForm()
    return render(request, 'recepcionistas/cadastrar_especialidade.html', {'form': form})


#Cadastro Exame
def exames_cadastrados(request):
    exames = ExameClinica.objects.all()
    return render(request, 'recepcionistas/exames_cadastrados.html', {'exames': exames})

def cadastrar_exame(request):
    if request.method == "POST":
        form = ExameClinicaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('exames_cadastrados')
    else:
        form = ExameClinicaForm()
    return render(request, 'recepcionistas/cadastrar_exame.html', {'form': form})

#Convênio
def convenios_cadastrados(request):
    convenios = Convenio.objects.all()
    return render(request, 'recepcionistas/convenios_cadastrados.html', {'convenios': convenios})

def cadastrar_convenio(request):
    if request.method == "POST":
        form = ConvenioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('convenios_cadastrados')
    else:
        form = ConvenioForm()
    return render(request, 'recepcionistas/cadastrar_convenio.html', {'form': form})


#Medico
def medicos_cadastrados(request):
    medicos = Medico.objects.all()
    return render(request, 'recepcionistas/medicos_cadastrados.html', {'medicos': medicos})

def cadastrar_medico(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('medicos_cadastrados')
        else:
            # Se o formulário não for válido, renderiza a página novamente com os erros
            return render(request, 'recepcionistas/cadastrar_medico.html', {'form': form})
    else:
        form = MedicoForm()
        
        return render(request, 'recepcionistas/cadastrar_medico.html', {'form': form})


#Exame
def exames_agendados(request):
    exames = ExameAgendado.objects.all()
    return render(request, 'recepcionistas/exames_agendados.html', {'exames': exames})

def agendar_exame(request):
    if request.method == "POST":
        form = ExameAgendadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('exames_agendados')
    else:
        form = ExameAgendadoForm()
    
    return render(request, 'pacientes/agendar_exame.html', {'form': form})


#Consulta
def consultas_agendadas(request):
    consultas = ConsultaAgendada.objects.all().order_by('-data_consulta')
    return render(request, 'recepcionistas/consultas_agendadas.html', {'consultas': consultas})

def agendar_consulta(request):
    if request.method == "POST":
        form = ConsultaAgendadaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('consultas_agendadas')
    else:
        form = ConsultaAgendadaForm()
    
    return render(request, 'pacientes/agendar_consulta.html', {'form': form})