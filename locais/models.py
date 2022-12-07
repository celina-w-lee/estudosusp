from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from enum import IntEnum
from django.db.models import Avg
from django.utils.timezone import datetime

class Local(models.Model):

    class Status(models.TextChoices):
        VAZIO = 'Vazio', _('Vazio')
        MEDIO = 'Médio', _('Médio')
        CHEIO = 'Cheio', _('Cheio')

    class SN(models.TextChoices):
        SIM = 'Sim', _('Sim')
        NAO = 'Não', _('Não')

    class Ruido(models.TextChoices):
        BAIXO = 'Baixo', _('Baixo')
        MEDIO = 'Médio', _('Médio')
        ALTO = 'Alto', _('Alto')

    class Permissoes(models.TextChoices):
        COMIDA = 'Permitido comida e água', _("Permitido comida e água")
        SEMCOMIDA = 'Não é permitida a ingestão de alimentos', _("Não é permitida a ingestão de alimentos")

    class Flexibilidade(models.TextChoices):
        MOCHILA = 'É permitido entrar de mochila', _("É permitido entrar de mochila")
        ARMARIO = 'É preciso guardar os pertences em armários', _("É preciso guardar os pertences em armários")

    class DiasFunc(models.TextChoices):
        SEGSEX = 'Segunda a sexta', _('Segunda a sexta')
        TODODIA = 'Todos os dias', _('Todos os dias')
        SEGSAB = 'Segunda a sábado', _('Segunda a sábado')
        OUTRO = 'Verificar no local', _('Verificar no local')

    nome = models.CharField(max_length=200)
    status = models.CharField(max_length=5, choices=Status.choices, default=Status.VAZIO)
    tomada = models.CharField(max_length=5, choices=SN.choices, default=SN.SIM)
    ruido = models.CharField(max_length=5, choices=Ruido.choices, default=Ruido.BAIXO)
    coberto = models.CharField(max_length=5, choices=SN.choices, default=SN.SIM)
    grupo = models.CharField(max_length=5, choices=SN.choices, default=SN.SIM)
    permissoes = models.CharField(max_length=50, choices=Permissoes.choices, default=Permissoes.COMIDA)
    flexibilidade = models.CharField(max_length=50, choices=Flexibilidade.choices, default=Flexibilidade.MOCHILA)
    imagem = models.ImageField(upload_to='uploads/', default='../media/uploads/study.jpg')
    inicio_func = models.TimeField()
    fim_func = models.TimeField()
    dias_func = models.CharField(max_length=50, choices=DiasFunc.choices, default=DiasFunc.SEGSEX)
    atualizacao = models.DateTimeField(auto_now=True)

    def average_rating(self):
        return Avaliacao.objects.filter(local=self).aggregate(Avg("rating"))["rating__avg"]

    def rating_count(self):
        return Avaliacao.objects.filter(local=self).count()

    def __str__(self):
        return f'{self.nome}'

class Avaliacao(models.Model):

    class TiposAval(IntEnum):
        PESSIMO = 1
        RUIM = 2
        MEDIO = 3
        BOM = 4
        OTIMO = 5

        @classmethod
        def choices(cls):
          return [(key.value, key.name) for key in cls]

    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=TiposAval.choices(), default=TiposAval.MEDIO)

    def __str__(self):
        return f"{self.local.nome}: {self.rating}"
