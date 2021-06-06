'''
tipo de dados
str - String  - textos  'Assim' ou "Assim"
int - inteiro - 1234556 - 0 - 10 - 50444
float - real/ponto flutuante 10.50 - 55.10 - 123.10
bool -booleano/logico true/false
'''
print('Armando', type('Luiz'))
print(10, type(10))
print(50.70, type(50.70))
print(10 == 10, type(10 == 10))
print(10 == 11, type(10 == 11))
print("L" == "L", type("L" == "L"))
print("L" == "l", type("L" == "l"))

print('Armando', type('Armando'), bool('Armando'))

# Conversão de tipos
print("Conversão de String para number", int('10'))
print("Conversão de String para number", float('10'))
print("Conversão de String para number", float('10.5'))
print("Conversão de String para number", float(10))

# Exercicio
print('Armando', type('Armando'))
print(25, type(25))
print(185.6, type(185.6))
print(25 >= 18, type(25 >= 18))
