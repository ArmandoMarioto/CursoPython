'''
Funções  - def em Python (Parte 1)
'''

def saudacao(msg ='Ola' , nome = 'usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg , nome)

saudacao(nome='Zezinho', msg = 'Hi')
saudacao('Oi', 'Jão')
saudacao('ola',  'Arm')
saudacao('Hello',  'Marioto')
saudacao('He',  'Neto')