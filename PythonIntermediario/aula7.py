'''
Tuplas em python
'''


#   tuplas nao sao editaveis
#   se quiser mudar o valor tem que transdorma em uma list
t1 = (1,2,3,'a','lus eadada')

print(type(t1), t1[2:])

t2 = 6,7,8,9
t3 = t1+ t2   #  pode se concatenar tuplas normalmente
#  *_ quer dizer que nao vou fazer mais nada com o restante
n1,n2,n3,*_,n10 = t3   #  desempacotando a tupla


print(n3 ,n10)