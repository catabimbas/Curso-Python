# Meu Código
"""
# Variáveis
peso_menor = 0
peso_maior = 0
# Repetição
for c in range(1, 6):
    # Variável float
    peso = float(input(f'Digite o {c+1}º Peso: '))
    # IFS
    if c == 0:
        peso_maior = peso_menor = peso
    if peso > peso_maior:
        peso_maior = peso
    elif peso < peso_menor:
        peso_menor = peso
# Print
print(f'''O prêmio de baleia foi de {peso_maior}
O prêmio de peso pena {peso_menor}''')
"""
# Código do curso

peso_menor = 0
peso_maior = 0
# Repetição
for c in range(1, 6):
    # Variável float
    peso = float(input(f'Digite o {c}º Peso: '))
    # IFS
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
# Print
print(f'''O prêmio de baleia foi de {peso_maior}
O prêmio de peso pena {peso_menor}''')
