cpf = input('Digite o CPF')
auxcpf = cpf.replace('.','')
#  425.554.408-52
auxcpf = auxcpf.split('-')
auxcpf, digitos = auxcpf
digito1 = digitos[0]
digito2 = digitos[1]
auxcpf = list(auxcpf)




print(auxcpf,digito1,digito2)