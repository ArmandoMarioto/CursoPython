'''

Funções (def) em python - return
'''

def f(var):
    print(var)

def dumb():
    return f


#   pode se fazer isso
var = dumb()('Olaaaaaa')
print(id(var) , id(f))