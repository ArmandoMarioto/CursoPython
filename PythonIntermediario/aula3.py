#  Exercicio 1

# def exibe(saudacao, nome):
#     print(saudacao, nome)
# exibe('Ola', 'Armando')

#  Exercicio 2

# def Soma(num1 , num2 ,num3):
#     print(num1+num2+num3)
# Soma(int(input()), int(input()), int(input()))

#  Exercicio 3

# def perc(valor,percetual):
#     return (valor * ((percetual/100)+1))
# print(perc(100,10))


def FizzBuzz (num):
    if num%5 == 0 and num%3 == 0:
        return 'FizzBuzz'
    elif num%5 == 0:
        return 'Buzz'
    elif num%3 == 0:
        return 'Fizz'

    return num

print(FizzBuzz(int(input())))
