# Variáveis float
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite outro valor: '))
# IFS Print
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Forma um triângulo')
    if n1 == n2 == n3:
        print('O triângulo é equilátero')
    elif n1 != n2 != n3 != n1:
        print('O triângulo é Escaleno')
    else:
        print('O triângulo é Isóseles')
else:
    print('Não forma um triângulo')
