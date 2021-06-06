'''
* Enumerate - Enumerar elementos da lista #list
'''

lista = [
    ['Edu', 'Dudu', 'Arm'],
    ['Jão', 'Maria', 'Eduarda'],
    ['Luiz', 'Felipe', 'Gabriel']
]

enumerada = list(enumerate(lista))

# print(enumerada[1][1][1])

for v1 in enumerate(lista,53):
    valor_enum , minha_lista = v1
    nome1,nome2,nome3 =minha_lista
    print(nome1,nome3)