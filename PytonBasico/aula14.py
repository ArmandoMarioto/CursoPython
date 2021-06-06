"""
while em Python
utilizando para realizar ações enquanto
uma condiçao for verdadeira

Requisitos :entender condições e operadores
"""

# x = 1
# while x <= 5:
#
#     if x == 3:
#         x += 1
#         continue
#         # break     pode se usar para PARAR
#
#     print(x)
#     x += 1
#
# print('Acabou')


# x = 0 #coluna
# y = 0 #linha
#
# while x < 10:
#     y = 0  # linha
#     while y < 5:
#         print(f' X vale {x} e Y Vale {y}')
#         y+= 1
#
#     x += 1
# print('Acabou!!!')


while True:
    num1 = input('Digite um numero.')
    num2 = input('Digite outro numero.')
    operador = input('Digite um operador.')

    if not num1.isnumeric() or not num2.isnumeric():
        print('VC precisa digitar um número.')
        continue

    num1 = int(num1)
    num2 = int(num2)
    if operador == '+':
        print(num1+num2)
    elif operador =='-':
        print(num1-num2)
    elif operador == '/':
        print(num1/num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador Invalido.')

