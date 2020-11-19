# Código do curso
from math import cos, sin, tan, radians
angulo = float(input('Digite um ângulo: '))
angulocos = cos(radians(angulo))
angulosen = sin(radians(angulo))
angulotan = tan(radians(angulo))
print('O ângulo de {} tem o Seno de {:.2f}\nO ângulo de {} tem o Cosseno de {:.2f}\nO ângulo de {} tem o Tangente de {:.2f}'.format(angulo, angulosen, angulo, angulocos, angulo, angulotan))
