# Meu Código
"""
numero = str(input('Digite um valor entre 0 até 9999: '))
print('Unidade: {}'.format(numero[0]))
print('Dezena: {}'.format(numero[1]))
print('Centena: {}'.format(numero[2]))
print('Milha: {}'.format(numero[3]))
"""
# Código Curso em Vídeo
numero = int(input('Digite um valor entre 0 até 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milha: {}'.format(m))
