# Importação
from random import choice
# Variáveis str
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
# Variáveis
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
# Cores
cor = {'fim': '\033[m',
       'amarelo': '\033[33m'}
print('{}{}{}'.format(cor['amarelo'], escolhido, cor['fim']))
