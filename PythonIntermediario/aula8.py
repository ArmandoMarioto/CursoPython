'''
Dicionarios em Python
'''


# d1 = {'chave1':'Valor da Chave'} #  quando se usa {} está criando um dicionario
# d2 = dict(chave2='Valor da Chave2', chave_d2 = 'Valor da chave da D2')
# d1['nova_chave'] = 'Valor da nova chave'
# print(d1)
# print(d2)
# print(d1['chave1'])
# print(d1['nova_chave'])
# print(d2['chave_d2'])
# print(d2.get('nomedachave') is not None)



#  apagando chave do dicionario

# del d1['chave1']


#   perguntar se um valor esta no dicionario
#   'valor' in d1.values()


# for k, v, in d2.items():
#     print(k, v)


clientes = {
    'cliente1' : {
       'nome' : 'Jão',
        'sobrenome' : 'Moreira',
    },'cliente2' : {
       'nome' : 'Luiz',
        'sobrenome' : 'Otavio',
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')