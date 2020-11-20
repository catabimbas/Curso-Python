# Meu Código
"""
# Variáveis int
PA = int(input('Digite um valor: '))
razao = int(input('Digite uma razão: '))
# Repetições
for c in range(0,10):
    print(f'{PA} ->', end=' ')
    PA = PA + razao
# Print
print('Acabou!')
"""
# Código do curso

# Variáveis int
PA = int(input('Digite um valor: '))
razao = int(input('Digite uma razão: '))
# Variável
decimo = PA + (10 - 1) * razao
# Repetições
for c in range(PA, decimo+razao, razao):
    print(f'{c} ', end='-> ')
# Print
print('Acabou!')
