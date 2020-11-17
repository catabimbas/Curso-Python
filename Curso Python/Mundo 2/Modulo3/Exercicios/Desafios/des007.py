fibonacci = int(input('Digite um valor: '))
mostrar = int(input('Digite quantas vezes quer mostrar: '))
rep = 0
razao = 1
while rep != mostrar:
    print(f'{fibonacci} -> {razao}',end=' -> ')
    fibonacci = fibonacci + razao
    razao = razao + fibonacci
    rep = rep + 1
print('Acabou!')
