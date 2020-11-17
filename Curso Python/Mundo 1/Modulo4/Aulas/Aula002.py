# Usando na formatação print dentro de variáveis
"""
nome = 'Guanabara'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print('Olá! Muito Prazer {}{}{}'.format(cores['azul'], nome, cores['limpa']))
----------------------------------------
nome = 'Guanabara'
print('Olá! Muito prazer {}{}{}'.format("\033[4;34m", nome, "\033[m"))
----------------------------------------
num1 = 3
num2 = 5
print(f'Os números listados são \033[33;45m{num1}\033[m e \033[34;42m{num2}\033[m')
----------------------------------------
num1 = 3
num2 = 5
print(f'Os números listados são \033[33m{num1}\033[m e \033[34m{num2}\033[m')
"""
# Usando a inversão
"""
print('\033[7;33;44mOlá, Mundo\033[m')
----------------------------------------
print('\033[7;30mOlá Mundo \033[m')
"""
# Mostrando outras cores
"""

print('\033[0;33;44mOlá, Mundo\033[m')
----------------------------------------
print('\033[1;30mOlá, Mundo \033[m')
----------------------------------------
print('\033[1;30;45mOlá, Mundo \033[m')
"""
# Formatação do fundo
"""
print('\033[1;31;43m Olá, mundo \033[m')
"""
# Estilo, texto e o fundo
"""
print('\033[1;31;43mOlá, Mundo')
"""
# Texto e o fundo
"""
print('\033[31;43mOlá, Mundo')
"""
# Apenas o texto
"""
print('\033[31m Olá, Mundo')
"""