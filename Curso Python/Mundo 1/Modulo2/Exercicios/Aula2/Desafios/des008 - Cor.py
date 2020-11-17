# Variável float
produto = float(input('Qual o valor do produto? '))
# Variáveis
desconto = produto * 5/100
desconto = produto - desconto
# Cores
cor = {'fim': '\033[m',
       'verde': '\033[32m'}
# Print
print('O produto com desconto fica {}{:.2f}{}'.format(cor['verde'], desconto, cor['fim']))
