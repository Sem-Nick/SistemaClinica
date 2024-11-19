from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Adicionar tipos de usuários
    USER_TYPE_CHOICES = (
        ('medico', 'Médico'),
        ('paciente', 'Paciente'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='paciente')