# Variáveis float
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite outro valor: '))
# Cores
cor = {'fim': '\033[m',
       'azul': '\033[34m',
       'vermelho': '\033[31m'}
# IFS
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print(f'{cor["azul"]}Forma um triângulo{cor["fim"]}')
else:
    print(f'{cor["vermelho"]}Não forma um triângulo{cor["fim"]}')
