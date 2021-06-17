'''
Aula 25 - Criando, lendo e escrevendo em arquivos
'''
import os
# file = open('aula25.txt','w+')
# file.write('Linha 1 \n')
# file.write('Linha 2 \n')
# file.write('Linha 3 \n')
# file.write('Linha 4 \n')
#
# file.seek(0,0)
# print('Lendo Linhas:')
# print(file.read())
# print('#############')
#
# file.seek(0,0)
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print('#############')
#
# file.seek(0,0)
# for linha in file:
#     print(linha)
# file.close()

with open('aula25.txt' ,'a+') as file:
    file.write('Outra linha.\n')
    file.seek(0,0)
    print(file.read())

# os.remove('aula25.txt') para excluir o arquivo, precisa do import os