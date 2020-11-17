# Variável int
numbase = int(input('Digite um valor: '))
# Variáveis
duble = numbase * 2
triple = numbase * 3
rq = numbase ** 0.5
# Cor
cor = {'fim': '\033[m',
       'cinza': '\033[37m',
       'verde': '\033[32m',
       'amarelo': '\033[33m'}
# Print
print('O dobro do valor: {}{}{} \nO triplo do valor: {}{}{} \nA raiz quadrada do valor: {}{:.2f}{}'.format(cor['verde'], duble, cor['fim'],
                                                                                                           cor['amarelo'], triple, cor['fim'],
                                                                                                           cor['cinza'], rq, cor['fim']))
