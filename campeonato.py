from patrocinador import Patrocinador
from atleta import Atleta

class Campeonato:
    def __init__ (self, nome, local, premiacao, categoria):
        self._nome = nome
        self._local = local
        self._premiacao = premiacao 
        self._patrocinadores = Patrocinador
        self._atletas = Atleta
        self._categoria = categoria

    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome (self, nome):
        self._nome = nome

    
    @property
    def local (self):
        return self._local

    @local.setter
    def local (self, local):
        self._local = local

    
    @property
    def premiacao (self):
        return self._premiacao

    @premiacao.setter
    def premiacao (self, premiacao):
        self._premiacao = premiacao

    @property
    def categoria (self):
        return self._categoria

    @categoria.setter
    def categoria (self, categoria):
        self._categoria = categoria