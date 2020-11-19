# Variáveis
numberOne = input('Primeiro número: ')
numberTwo = input('Segundo número: ')
# Somar e Converter em Number
numberAll = int(numberOne) + int(numberTwo)
# Cor
cor = {'amarelo': '\033[33m',
       'fim': '\033[m'}
# Texto
print('A soma desses valores é: {}{}{}'.format(cor['amarelo'], numberAll, cor['fim']))
