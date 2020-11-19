# Variáveis int
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
# Cores
cor = {'fim': '\033[m',
       'amarelo': '\033[33m',
       'vermelho': '\033[31m'}
# IFS
# Maiores
if num1 > num2:
    if num1 > num3:
        print(f'{cor["amarelo"]}1º Valor é maior{cor["fim"]}')
else:
    if num2 > num3:
        print(f'{cor["amarelo"]}2º Valor é maior{cor["fim"]}')
    else:
        print(f'{cor["amarelo"]}3º Valor é maior{cor["fim"]}')
# Menores
if num1 < num2:
    if num1 < num3:
        print(f'{cor["vermelho"]}1º Valor é menor{cor["fim"]}')
else:
    if num2 < num3:
        print(f'{cor["vermelho"]}2º Valor é menor{cor["fim"]}')
    else:
        print(f'{cor["vermelho"]}3º Valor é menor{cor["fim"]}')
