from django import forms
from .models import Paciente, Medico, Funcionario, ExameClinica, EspecialidadeClinica, ExameAgendado, ConsultaAgendada, Convenio

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento', 'endereco', 'email', 'telefone']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'data_nascimento', 'endereco', 'email', 'telefone']


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'cpf', 'especialidade', 'data_nascimento', 'endereco', 'email', 'telefone', 'senha']


class ExameAgendadoForm(forms.ModelForm):
    class Meta:
        model = ExameAgendado
        fields = ['exame', 'paciente', 'sexo', 'convenio', 'medico_preferencia', 'data_consulta', 'horario']
        widgets = {
            'data_consulta': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'})
        }


class ConsultaAgendadaForm(forms.ModelForm):
    class Meta:
        model = ConsultaAgendada
        fields = ['consulta', 'paciente', 'sexo', 'convenio', 'medico_preferencia', 'data_consulta', 'horario']
        widgets = {
            'data_consulta': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'})
        }
    

class ConvenioForm(forms.ModelForm):
    class Meta:
        model = Convenio
        fields = ['codigo', 'nome', 'ativo', 'validade', 'contato', 'cobertura']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }


class ExameClinicaForm(forms.ModelForm):
    class Meta:
        model = ExameClinica
        fields = ['codigo', 'nome', 'descricao', 'valor', 'ativo']


class EspecialidadeClinicaForm(forms.ModelForm):
    class Meta:
        model = EspecialidadeClinica
        fields = ['codigo', 'nome', 'descricao', 'valor']
