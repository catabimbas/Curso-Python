# Digite algum nome
nome = str(input('Digite o nome completo: '))
# Variáveis
nomelist = nome.split()
nome2 = nome.rfind(max(' '))
nome2C = nome[nome2:].lstrip()
# Prints Formatadas
print(f'O nome completo que você digitou: {nome}')
print(f'O seu Primeiro nome: {nomelist[0]}')
print(f'O seu último nome: {nome2C}')
