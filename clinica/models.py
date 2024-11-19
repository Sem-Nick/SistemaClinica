from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=128)

    # def set_senha(self, raw_password):
    #     self.senha = make_password(raw_password)

    def __str__(self): 
        return self.nome
    
class Convenio(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=True)
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    validade = models.DateField(null=True)
    contato = models.CharField(max_length=255, null=True)
    cobertura = models.CharField(max_length=255, null=True)

class ExameClinica(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    descricao = models.TextField(null=True)

class EspecialidadeClinica(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    descricao = models.TextField(null=True)

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    especialidade = models.ForeignKey(EspecialidadeClinica, on_delete=models.CASCADE, null=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=128)


class ExameAgendado(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    exame = models.ForeignKey(ExameClinica, on_delete=models.CASCADE, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)  # Referência ao paciente
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, null=True)
    medico_preferencia = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    data_consulta = models.DateField()
    horario = models.TimeField(default='08:00')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')

    def __str__(self):
        return self.nome
    

class ConsultaAgendada(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    consulta = models.ForeignKey(EspecialidadeClinica, on_delete=models.CASCADE, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, null=True)
    medico_preferencia = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    data_consulta = models.DateField()
    horario = models.TimeField(default='08:00')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')