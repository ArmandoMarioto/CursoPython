'''
Zip - Unindo iteraveis
Zip_longest  - Itertools
'''
from itertools import zip_longest, count

indice = count()

cidades = ['São Paulo', 'Belo Horizonte', 'Saalvador', 'Monte Belo']
estados = ['SP','MG','BA']

cidades_estados = zip(indice,cidades,estados)
# cidades_estados = zip_longest(indice,cidades,estados,fillvalue='Estado')

for valor in cidades_estados:
    print(valor)