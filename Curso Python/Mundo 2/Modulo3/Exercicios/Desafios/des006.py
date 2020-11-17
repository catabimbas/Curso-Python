PA = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
rep_end = int(input('Quer mostrar quantos termos? '))
rep = 0
while rep != rep_end:
    print(PA, end=' -> ')
    PA = PA + razao
    rep += 1
print('Acabou!')
