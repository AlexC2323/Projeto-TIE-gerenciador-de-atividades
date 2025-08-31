from django.db import models
from django.utils import timezone

class Atividade(models.Model):
    opcoes_status = (
        ('concluida', 'Concluída'),
        ('pendente', 'Pendente'),
        ('adiada', 'Adiada'),
    )

    opcoes_categoria = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feita', 'Precisa ser feita'),
    )

    descricao = models.CharField(max_length=500)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=100, choices=opcoes_categoria, default='importante')
    status = models.CharField(max_length=50, choices=opcoes_status, default='pendente')
    data_vencimento = models.DateField(default=timezone.now) 