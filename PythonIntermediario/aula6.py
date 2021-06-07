'''
Expressões lambda (funções anonimas) em python
E como ordena uma lista
'''

# a = lambda x ,y : x * y
#
# print(a(2,2))


lista = [
    ['p1',13],
    ['p2',155],
    ['p3',56],
    ['p4',87],
    ['p5',50],
]


# sort ordena a lista em python
# lista.sort(key= lambda item: item[1], reverse=True)  #use o lambda para ordena e o reserve para ordena ao contrario
print(sorted(lista , key = lambda i: i[0])) #assim ordena , mas nao muda na lista,o .sort ordena na list