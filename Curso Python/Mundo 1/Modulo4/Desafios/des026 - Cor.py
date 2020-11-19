# Importação
from random import randint
# Variável int
print('----------------------')
print('     Adivinhador')
print('----------------------')
numerosort = int(input('Adivinhe qual número vai sair entre 1 e 5: '))
# Variáveis
numeroAleatorio = randint(1, 5)
numeroAleatorio = numeroAleatorio == numerosort
# Cores
cor = {'fim': '\033[m',
       'erro': '\033[31m',
       'verdade': '\033[32m'}
# IFS
if numeroAleatorio:
    # Prints
    print('{}Parabéns, você acertou!{}'.format(cor['verdade'], cor['fim']))
else:
    # Prints
    print('{}Você errou!{}'.format(cor['erro'], cor['fim']))
# Print
print('Tente novamente apertando Shift+F10')
