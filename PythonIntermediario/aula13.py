'''
Aula 13 - Geradores ,iteradores e iteraveis
'''
import sys

# lista = [0,1,2,3,4]
# lista = iter(lista)
#
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
#
# print(hasattr(lista, '__next__'))


l1 = [x for x in range(100000)]
l2 = (x for x in range(100000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
#
# for v in l2:
#     print(v)