
#   Aula 10 - Conjuntos
#   add (adicionar), update(atualizar), clear, discard
#   union | (une)
#   intersection & (todos os elementos presentes nos dois sets)
#   difference - (elemtos apenas no set da esquerda)
#   symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

# o conjunto elimina os valores repitidos
s1 = {1,2,3,4,5,6}
s2 = {1,5,6,47,55,64}
s3 = {1,2,36,54,45,26}
s1.add(100)
s1.discard(5)

s4 = s1 | s3
print(s4)
s4 = s3 & s2
print(s4)
s4 = s3 - s2
print(s4)
s4 = s3 ^ s2
print(s4)

