PA = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
rep_end = int(input('Quer mostrar quantos termos? '))
rep = 0
while rep_end != 0:
    rep = 0
    while rep != rep_end:
        print(PA, end=' -> ')
        PA = PA + razao
        rep += 1
    print('Pausa')
    rep_end = int(input('Quantos termos mostrar a mais? '))
print('Acabou!')
