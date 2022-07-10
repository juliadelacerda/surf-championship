class Atleta:
    def __init__(self, nome, idade, pontuacao):
        self._nome = nome
        self._idade = idade
        self._pontuacao = pontuacao

    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome (self, nome):
        self._nome = nome


    @property
    def idade (self):
        return self._idade

    @idade.setter
    def idade (self, idade):
        self._idade = idade

    
    @property
    def pontuacao (self):
        return self._pontuacao

    @pontuacao.setter
    def pontuacao (self, pontuacao):
        self._pontuacao = pontuacao


    def vencedor (self):
        pass