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
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente'))
h1 = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h1))
