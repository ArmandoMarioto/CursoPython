'''
For in em Python
iterando strings com for
Função range(start = 0, stop , step=1)
'''


texto = 'Python'
nova_string = ''

# for n in range(1, 11, 5):   # crescente
#     print(n)
#
# for n in range(20, 9, -1):   # Decrecente
#     print(n)


for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)