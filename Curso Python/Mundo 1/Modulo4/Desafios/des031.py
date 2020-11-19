num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
# Menores
if num1 > num2:
    if num1 > num3:
        print('1º Valor é maior')
else:
    if num2 > num3:
        print('2º Valor é maior')
    else:
        print('3º Valor é maior')
# Maiores
if num1 < num2:
    if num1 < num3:
        print('1º Valor é menor')
else:
    if num2 < num3:
        print('2º Valor é menor')
    else:
        print('3º Valor é menor')
