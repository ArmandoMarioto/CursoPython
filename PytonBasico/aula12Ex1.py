"""
# Exercicio 1
num = input('Digite um número Inteiro. ')

if num.isnumeric():
    num = int(num)
    if (num % 2) == 0:
        print(f'{num} é um numero par. ')
    else:
        print(f'{num} é um numero impar. ')
else:
    print(f'{num} Não é um numero inteiro. ')
"""
"""
# Exercicio 2
hora = input('Digite o Horario: ')
if hora.isnumeric():
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom dia!!!')
    elif 11 < hora <= 17:
        print('Boa Tarde!!!')
    elif 17 < hora <= 23:
        print('Boa Noite!!!')
else:
    print(f'{hora} Não é uma hora certa. ')
"""

# Exercicio 3

nome = input('Digite o primeiro nome de usuario.')
if len(nome) <= 4 :
    print('Seu nome é curto. ')
elif len(nome) <= 6 :
    print('Seu nome é normal. ')
else:
    print('Seu nome é muito grande. ')