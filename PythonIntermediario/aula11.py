'''
    Aula 11 - list comprehension
'''

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

print(ex1)
print(ex2)
print(ex3)

l2 = ['Luiz', 'Jão', 'Maria']
ex4 = [v.replace('a','@') for v in l2]
print(ex4)

l3= list(range(100))
ex5 = [v for v in l3 if v % 3 == 0]
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex5)
print(ex6)