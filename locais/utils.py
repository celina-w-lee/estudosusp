# https://medium.com/@bencleary/using-enums-as-django-model-choices-96c4cbb78b2e

from enum import IntEnum

class Status(IntEnum):
  VAZIO = 1
  MEDIO = 2
  CHEIO = 3
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Tomada(IntEnum):
  SIM = 1
  NAO = 2
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Ruido(IntEnum):
  BAIXO = 1
  MEDIO = 2
  ALTO = 3
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Coberto(IntEnum):
  SIM = 1
  NAO = 2
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Grupo(IntEnum):
  SIM = 1
  NAO = 2
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Permissoes(IntEnum):
  COMIDA = 1 #"Permitido comida e água"
  SEMCOMIDA = 2 #"Não é permitida a ingestão de alimentos"

  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Flexibilidade(IntEnum):
  MOCHILA = 1 #"É permitido entrar de mochila"
  ARMARIO = 2 #"É preciso guardar os pertences em armários"

  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]
