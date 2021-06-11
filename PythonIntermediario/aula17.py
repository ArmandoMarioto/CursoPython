'''
Aula 17 - Groupby -agrupando valores
'''
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'Claudia', 'nota': 'A'},
    {'nome': 'Gabriel', 'nota': 'E'},
    {'nome': 'Felipe', 'nota': 'B'},
    {'nome': 'Mario', 'nota': 'B'},
    {'nome': 'Fernando', 'nota': 'C'},
    {'nome': 'Joaquin', 'nota': 'E'},
]
ordena = lambda item: item['nota']
alunos .sort(key = ordena)
alunos_agrupados = groupby(alunos,ordena)

for agrupamento,valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
# for aluno in alunos:
#     print(aluno)