class Pessoa:  # super classe
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Falando....')


class Cliente(Pessoa):# herdando da super,Cliente é classe filha
    def comprar(self):
        print(f'{self.nome} está comprando...')
class Aluno(Pessoa):# herdando da super,Aluno é classe filha
    def estudar(self):
        print(f'{self.nome} está estudando....')