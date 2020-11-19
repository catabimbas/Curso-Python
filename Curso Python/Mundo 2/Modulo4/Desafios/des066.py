import random
numPI = vitoria = 0
parOuImpar = piPc = ''
while True:
    numPI = int(input('Qual o seu número? '))
    parOuImpar = str(input('Par ou Impar? [P/I] ').upper())
    numPC = random.randint(1, numPI)
    res = numPI + numPC
    if parOuImpar == 'P':
        piPc = 'I'
    elif parOuImpar == 'I':
        piPc = 'P'
    if res % 2 == 0 and parOuImpar == 'P':
        vitoria += 1
        piPc = 'I'
        print('Você ganhou!')
    elif res % 2 == 1 and parOuImpar == 'I':
        vitoria += 1
    else:
        print('Você perdeu!')
        print(f'O computador escolheu {piPc} e você escolheu {parOuImpar} e no total, deu {res}')
        break
    print(f'O computador escolheu {piPc} e você escolheu {parOuImpar} e no total, deu {res}')
print(f'O total de vitórias foram de {vitoria} vitórias consecutivas')
