'''
Aula 22 - Mais uma aula de TRY
'''

def converte(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converte(input('Digite um numero'))

    if numero is None:
        print('Erro: isso nao é um numero')
    else:
        print(numero * 2)
