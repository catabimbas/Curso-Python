# Variável int
ano = int(input('Digite o ano: '))
# Variável
anonovo = ano % 4
# Cores
cor = {'fim': '\033[m',
       'roxo': '\033[35m',
       'branco': '\033[30m'}
# IFS Print
if anonovo == 0:
    print(f'{cor["branco"]}Este ano é bissexto {cor["fim"]}')
else:
    print(f'{cor["roxo"]}Este ano não é bissexto {cor["fim"]}')
