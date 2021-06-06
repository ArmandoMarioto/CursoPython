nome = 'Armando Marioto'
idade = 25
altura = 1.85
peso = 90
e_maior = idade >= 18

imc = peso / (altura*2)

# 3 jeitos de escrever a mesma coisa
print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

print('{1} tem {2} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
