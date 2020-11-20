# Variável int
kmviagem = int(input('Quantos Km tem a viagem? '))
# Cores
cor = {'fim': '\033[m',
       'verde': '\033[32m'}
# IFS Print
if kmviagem < 200:
    passagem = kmviagem * 0.50
else:
    passagem = kmviagem * 0.45
# Print
print(f'O preço da viagem fica por {cor["verde"]}{passagem}{cor["fim"]}')
