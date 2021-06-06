nome = 'Armando Marioto'
idade = 25
altura = 1.85
peso = 90.5
ano_atual = 2021
imc = (peso / (altura**2))
e_maior = idade >= 18
ano_nascimento = ano_atual - idade


print(f'{nome} tem {idade} anos de idade, sua altura é {altura} ,Peso é {peso} ,Nasceu no ano {ano_nascimento} e seu IMC é : {imc:.2f}')

