# Importação
from random import choice
# Variável str
player = str(input('Escolhe: Pedra, papel ou tesoura? ')).capitalize()
input('Pedra')
input('Papel')
# Variáveis
lista = ['Pedra', 'Papel', 'Tesoura']
CPU = choice(lista)
# IFS
# Papel vs Pedra || Player
if CPU == 'Pedra' and player == 'Papel':
    print('Tesoura')
    print('Você ganhou do computador!')
# Papel vs Pedra || CPU
elif CPU == 'Papel' and player == 'Pedra':
    print('Tesoura')
    print('Você perdeu do computador!')
# Pedra vs Tesoura || Player
if CPU == 'Pedra' and player == 'Tesoura':
    print('Tesoura')
    print('Você perdeu do computador!')
# Pedra vs Tesoura || CPU
elif CPU == 'Tesoura' and player == 'Pedra':
    print('Tesoura')
    print('Você ganhou do computador!')
# Tesoura vs Papel || Player
if CPU == 'Papel' and player == 'Tesoura':
    print('Tesoura')
    print('Você ganhou do computador!')
# Tesoura vs Papel || CPU
elif CPU == 'Tesoura' and player == 'Papel':
    print('Tesoura')
    print('Você perdeu do computador!')
# Empate
elif CPU == player:
    print('Tesoura')
    print('Você empatou com o computador!')
# Print
print(f'''-----------------------------
Você usou {player}
E o computador usou {CPU}
-----------------------------''')
