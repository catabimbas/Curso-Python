# Instalando módulos
# Importanto módulo emoji
import emoji
print(emoji.emojize("Olá mundo :sunglasses:", use_aliases=True))
# Os módulos acima não são possiveis de fazer no celular
# Importanto módulo random
"""
import random
num = random.random()
print(num)
"""

# Forma 3 de formatar, usando resumo
"""
import math
num = int(input('Digite um número'))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))
"""
# Forma 2 de formatar, arredondar baixo
"""
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, math.floor(raiz)))
"""
# Forma 1 de formatar, arredondar pra cima
"""
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, math.cell(raiz)))
"""

# Forma 2 de selecionar comandos de uma biblioteca
"""
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
"""
# Forma 1 de selecionar comandos de uma biblioteca
"""
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
"""

# Primeira forma de usar bibliotecas python
"""
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
"""