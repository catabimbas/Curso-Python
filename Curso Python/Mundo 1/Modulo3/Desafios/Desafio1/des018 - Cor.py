# Importação
from random import sample
# Variáveis str
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
# Variáveis
lista = [n1, n2, n3, n4]
escolhido = sample(lista, 4)
# Cores
cor = {'fim': '\033[m',
       'amarelo': '\033[33m',
       'roxo': '\033[35m',
       'ciano': '\033[36m',
       'cinza': '\033[37m'}

# Print
print('Os sorteados para apresentarem os trabalhos \nPrimeiro: {}{}{} \nSegundo: {}{}{} \nTerceiro: {}{}{}\nQuarto: {}{}{}'.format(cor['amarelo'], escolhido[0], cor['fim'], cor['roxo'], escolhido[1], cor['fim'], cor['ciano'], escolhido[2], cor['fim'], cor['cinza'], escolhido[3], cor['fim']))
