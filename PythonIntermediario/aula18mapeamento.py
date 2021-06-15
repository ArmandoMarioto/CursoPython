from aula18Dados import produtos, pessoas, lista


# nova_lista = map(lambda x: x * 2, lista)
# print(lista)
# nova_lista = [x * 2 for x in lista]
# print(list(nova_lista))

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
#
#
# novos_produtos = map(aumenta_preco, produtos)
#
# for produto in novos_produtos:
#     print(produto)

#
# nomes = map(lambda p: p['nome'],pessoas)
# for p in nomes:
#     print(p)


# nova_lista = filter(lambda x: x > 5,lista)  #  Com função filter
# nova_lista = [x for x in lista if x > 5]  #  Com list comprehension
# print(list(nova_lista))


# nova_produtos = filter(lambda x : x['preco']>10,produtos)
#
# for produto in nova_produtos:
#     print(produto)

def filtra(pessoa):
    if pessoa['idade'] <= 18:
        return True
    return False

nova_lista = filter(filtra,pessoas)

for pessoa in nova_lista:
    print(pessoa)