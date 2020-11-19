# Variável
soma = 0
# Repetição
for c in range(1, 7):
    num = int(input('Digite um número: '))
    # IF
    if num % 2 == 0:
        soma += num
# Print
print(f'O valor somado é igual a {soma}')
