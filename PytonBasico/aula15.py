'''
While / Else
contadores
acumuladores
'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador += contador
    contador += 1
else:   # Em python pode usar ELSE no while
    print('Cheguei Aqui no ELse.')
