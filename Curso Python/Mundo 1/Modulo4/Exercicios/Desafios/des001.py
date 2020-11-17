import random
numeroAleatorio = random.randint(1, 5)
print('----------------------')
print('     Adivinhador')
print('----------------------')
numerosort = int(input('Adivinhe qual número vai sair entre 1 e 5: '))
if numeroAleatorio == numerosort:
    print('Parabéns, você acertou!')
else:
    print('Você errou!')
print('Tente novamente apertando Shift+F10')
