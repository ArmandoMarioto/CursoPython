'''
    Aula 8 - Herança simples
'''
from classes import *

c1 = Cliente('Luiz',45)
print(c1.nome)
c1.falar()
c1.comprar()
print('\n ##########################\n')
a1 = Aluno('Armando',25)
print(a1.nome)
a1.falar()
a1.estudar()