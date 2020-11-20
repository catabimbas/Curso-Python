# Importação
from math import factorial
# Variável int
fatorial = int(input('Digite um valor: '))
# Variáveis
rep = fatorial
fatorial = factorial(fatorial)
# Repetição
while rep != 1:
    print(f'{rep}', end='x')
    rep -= 1
# Print
print(f'{rep}',end='')
print(f' = {fatorial}')
