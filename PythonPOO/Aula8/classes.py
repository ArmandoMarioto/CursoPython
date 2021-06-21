class Pessoa:  # super classe
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Falando....')


class Cliente(Pessoa):# herdando da super,Cliente é classe filha
    def comprar(self):
        print(f'{self.nome} está comprando...')

    def falar(self):
        print('Estou em CLIENTE.')

class ClienteVIP(Cliente):#Sobrepondo o metodo falar
    def __init__(self,nome, idade,sobrenome):
        super().__init__(nome,idade)
        self.sobrenome = sobrenome



    def falar(self):
        #  super().falar()# usando o metodo da Super classe.
        Pessoa.falar(self)# usando o metodo da classe Pessoa.
        Cliente.falar(self)# usando o metodo da classe Cliente.
        print(f'{self.nome} {self.sobrenome} está falando.......')



class Aluno(Pessoa):# herdando da super,Aluno é classe filha
    def estudar(self):
        print(f'{self.nome} está estudando....')