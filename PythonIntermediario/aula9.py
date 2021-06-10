'''
Aula 9 - Perguntas e respostas usando dicionario.
'''
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quantos é 2+2? ',
        'repostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '6',
        },
        'resposta_certa': 'b',
    },'Pergunta 2': {
        'pergunta': 'Quantos é 3*3? ',
        'repostas': {
            'a': '10',
            'b': '8',
            'c': '11',
            'd': '9',
        },
        'resposta_certa': 'd',
    },'Pergunta 3': {
        'pergunta': 'Quantos é 2/2? ',
        'repostas': {
            'a': '1',
            'b': '-4',
            'c': '0',
            'd': '6',
        },
        'resposta_certa': 'a',
    },
}

for pk,pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas: ')

    for rk,rv in pv['repostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Vc Acertouu!!!!')
    else:
        print(f'Vc Errou , resposta certa era : {pv["resposta_certa"]}')
    print()