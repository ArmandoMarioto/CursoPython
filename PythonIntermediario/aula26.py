'''
Aula 26 - Decoradoras
'''

def master(funcao):  #  Função decoradora
    def slave():
        print('Agora estou decorada')
        funcao()
    return slave


@master    #  decorando
def fala_oi():
    print('Oi')

fala_oi()
