'''
Combinations , permutations e product - itertools
combinação - ordem não importa
permutação - ordem importa
ambos não repetem valores unicos
produto - ordem importa e repete varios unicos
'''

from itertools import combinations,permutations, product

pessoas = ['luiz','andre','fernando','jao','gabriel','augusto','ze']

for grupo in product(pessoas,repeat=2):
    print(grupo)