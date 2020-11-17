# Variáveis int
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
# Variável
media = (nota1 + nota2) / 2
# Cor
cor = {'fim': '\033[m',
       'roxo': '\033[35m'}
# Print
print('A média do aluno: {}{}{}'.format(cor['roxo'], media, cor['fim']))
