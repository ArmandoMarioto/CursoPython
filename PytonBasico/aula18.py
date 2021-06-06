'''
Listas em Python
fatiamento
append, insert , pop , del , clear , extend , +
min , max
range
'''

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
# lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G',10.5]
#
# l2.append('AA')
# l3.extend(l2)
# l1.insert(0, ' Banana')
#
# print(l3)
# l3.pop()
# print(l3)

# lista[-1] = 'qualquer coisa'
# print(lista[-1])
# print(lista)
# fatiamento
# print(lista[3:6])
# print(lista[2:])
# print(lista[::2])
# print(lista[::-1])

# l2 = list(range(0, 100, 8))
# print(l2)
# for valor in l2:
#     print(valor)

# l2 = ['String', True, 10, -20.5]
# for elem in l2:
#     print(f'O tipo de {elem} é : {type(elem)}')
digitadas = []
secreto = ' pamonha'
while True:
    letra = input('Digite uma Letra: ')

    if len(letra) > 1:
        print('Ahh isso nao vale,  digite apenas uma letra.')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhulll, a letra "{letra}" existe na palavra secreta. ')
    else:
        print(f'AFFFFz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()
    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Que legal, vc GANHOU !!!! A palavra era {secreto}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

