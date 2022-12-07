from django.forms import ModelForm
from .models import Local, Avaliacao

class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields = [
            'nome',
            'status',
            'tomada',
            'ruido',
            'coberto',
            'grupo',
            'permissoes',
            'flexibilidade',
            'imagem',
            'inicio_func',
            'fim_func',
            'dias_func',
        ]
        labels = {
            'name': 'Título',
            'release_year': 'Data de Lançamento',
            'poster_url': 'URL do Poster',
            'nome': 'Nome do Local',
            'status': 'Status do Local',
            'tomada': 'Tomadas Disponíveis',
            'ruido' : 'Nivel de Ruído',
            'coberto': 'Local Coberto',
            'grupo': 'Estudo em Grupo',
            'permissoes': 'Permissões',
            'flexibilidade': 'Flexibilidade',
            'imagem' : 'Imagem do Local',
            'inicio_func': 'Início do funcionamento',
            'fim_func': "Fim do funcionamento",
            'dias_func': 'Dias de funcionamento',
        }

class RateForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = [
            'rating',
        ]
        labels = {
            'rating': 'Avaliação',
        }