from random import randint
player = int(input('Tente adivinha qual o número o computador sorteou entre 1 e 10: '))
CPU = randint(1, 10)
tentativas = 0
while player != CPU:
    player = int(input('Você errou, tente novamente: '))
    tentativas += 1
print('Você acertou')
if tentativas == 0:
    print('Você acertou de primeira')
else:
    print(f'Você repetiu {tentativas} vezes até acerta o número sorteado')
