PA = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
rep = 0
while rep != 10:
    rep += 1
    print(PA,end=' -> ')
    PA = PA + razao
print('Acabou!')
