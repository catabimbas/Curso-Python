# Variável int
carteira = int(input('Quantos reais você tem: '))
# Variável
carteira = carteira / 3.27
# Cores
cor = {'fim': '\033[m',
       'verde': '\033[32m'}
# Print
print('Com o dinheiro atual, você tem {}{:.2f} doláres{}'.format(cor['verde'], carteira, cor['fim']))
