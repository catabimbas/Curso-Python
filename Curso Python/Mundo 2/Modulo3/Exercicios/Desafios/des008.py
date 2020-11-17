numero = 0
res = 0
digitados = 0
while numero != 999:
    numero = int(input('Digite um valor: '))
    res += numero
    digitados += 1
print(f'O total de números digitados foi de {digitados - 1} (Sem contar o 999) e a soma entre os números digitados foi de {res - 999}')
