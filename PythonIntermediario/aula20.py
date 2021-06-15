'''
Aula 20 - Try , except - Tratando exceções em python
'''

try:
    print()
except NameError as erro:
    print('Erro', erro)
except IndexError as erro:
    print('Erro', erro)
except Exception as erro:
    print('Erro', erro)
else:
    print('Excecuta sempre que o bloco Try com executado sem erro.')
finally:
    print('Executa independente se ocorreu erro ou não no TRY.')

print('bora continuar')