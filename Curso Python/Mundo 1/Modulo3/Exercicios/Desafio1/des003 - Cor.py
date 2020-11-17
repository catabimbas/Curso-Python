# Código do curso
# Importação
from math import cos, sin, tan, radians
# Variável
angulo = float(input('Digite um ângulo: '))
# Variáveis
angulocos = cos(radians(angulo))
angulosen = sin(radians(angulo))
angulotan = tan(radians(angulo))
# Cores
cor = {'fim': '\033[m',
       'verde': '\033[32m',
       'amarelo': '\033[33m'}
# Print
print('O ângulo de {}{}{} tem o Seno de {}{:.2f}{}\nO ângulo de {}{}{} tem o Cosseno de {}{:.2f}{}\nO ângulo de {}{}{} tem o Tangente de {}{:.2f}{}'.format(cor['verde'], angulo, cor['fim'], cor['amarelo'], angulosen, cor['fim'],
                                                                                                                                    cor['verde'], angulo, cor['fim'], cor['amarelo'], angulocos, cor['fim'],
                                                                                                                                    cor['verde'], angulo, cor['fim'], cor['amarelo'], angulotan, cor['fim']))
