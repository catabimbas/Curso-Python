# Variável int
numeroIP = int(input('Digite um número: '))
# Variável
numeroT = numeroIP / 2
# Cores
cor = {'fim': '\033[m',
       'branco': '\033[30m'}
# IFS Print
if numeroT % 1:
    # Print
    print(f'O número digitado é {cor["branco"]}impar{cor["fim"]}')
else:
    # Print
    print(f'O número digitado é {cor["branco"]}par{cor["fim"]}')
