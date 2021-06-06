'''
Splint, join , Enumerate em python
* Splint - dividir uma string #str
* Join - Juntar uma lista #str
* Enumerar elementos da lista #iteraveis
'''


string = 'o Brasil é o país do futebol, o Brasil é penta. '
lista1 = string.split(' ')
lista2 = string.split(',')
palavra = ''
contagem = 0
# for valor in lista1:
#     # print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase. ')
#     qtd_vezes = lista1.count(valor)
#     if qtd_vezes> contagem:
#         contagem = qtd_vezes
#         palavra = valor
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')


# for valor in lista2:
#     #  strip() Tira os espaços do começo e do final da String
#     #  capitalize() coloca maiusculo o primeiro caracter.
#
#     print(valor.strip().capitalize())


# lista3 = string.split(' ')
# string2 = '*'.join(lista3)
#
# print(string2)

lista = string.split(' ')

for indice,valor in enumerate(lista):
    print(indice, valor, lista[indice])