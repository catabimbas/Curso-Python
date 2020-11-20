# Variável
soma = 0
cont = 0
# Repetição
for c in range(1,501, 2):
    # IF
    if c % 3 == 0:
        cont += 1
        soma = soma + c
# Print
print(f'A soma de todos os valores solicitados é {soma} e teve {cont} números contados')
