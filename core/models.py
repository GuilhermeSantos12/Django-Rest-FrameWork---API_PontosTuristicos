from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from enderecos.models import Enderecos
# Create your models here.

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=300)
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentarios)
    avaliacao = models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(Enderecos, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    