'''
Funções (def) em Python - *args **kwargs
'''


# def func(a1, a2, a3, a4, a5, nome=None):
#     print(a1,a2,a3,a4,a5,nome)
#
# func(1,2,3,4,5,nome="Armando")


def func(*args):
     print(args)
    # print(args[0])
    # print(args[-1])
    # print(len(args))
    # # args[0] = 20 #    não pode atribuir valor ao uma tupla.
    # args =list(args)
    # args[0] = 20   #  depois que transforma em lista , pode se mudar o valor.
    # for v in args:
    #     print(v)

def fun(**kwargs):
    print(kwargs['nome'],kwargs['sobrenome'])
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2)
fun(nome="Armando", sobrenome="Marioto", idade=25)