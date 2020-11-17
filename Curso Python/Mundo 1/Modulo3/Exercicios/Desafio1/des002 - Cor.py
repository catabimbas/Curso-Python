# Meu código
"""
from math import sqrt
co = float(input('Digite um valor pro cateto oposto: '))
ca = float(input('Digite um valor pro cateto adjacente: '))
co2 = co * co
ca2 = ca * ca
rqm = (ca2 + co2)
rq = sqrt(rqm)
print("O valor da hipotenusa é de {:.2f}".format(rq))
"""
# Código do curso
# Importação
from math import hypot
# Variáveis float
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# Variáveis
h1 = hypot(co, ca)
# Cores
cor = {'fim': '\033[m',
       'ciano': '\033[36m'}
# Print
print('A hipotenusa vai medir {}{:.2f}{}'.format(cor['ciano'], h1, cor['fim']))
