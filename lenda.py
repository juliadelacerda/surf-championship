from atleta import Atleta

class Lenda (Atleta):
    def __init__ (self, nome, idade, pontuacao):
        super().__init__(nome, idade, pontuacao)


    def vencedor (self):
        if self._pontuacao >= 100:
            return True