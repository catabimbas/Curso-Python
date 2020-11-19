# Importações
from math import floor
# Variável float
real = float(input('Digite um número real: '))
# Variável
floreal = floor(real)
# Cores
cor = {'fim': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m'}
# Print
print('O valor {}{}{} na forma inteira fica {}{}{}'.format(cor['vermelho'], real, cor['fim'],
                                                           cor['verde'], floreal, cor['fim']))
