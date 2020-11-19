# Variável
numero = int(input('Digite um valor: '))
# Cor
cor = {'fim': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'branco': '\033[30m'}
# Print
print('O antecessor de {}{}{} é {}{}{}\nO sucessor de {}{}{} é {}{}{}'.format(cor['branco'], numero, cor['fim'],
                                                                            cor['vermelho'], numero-1, cor['fim'],
                                                                            cor['branco'], numero, cor['fim'],
                                                                            cor['verde'], numero+1, cor['fim']))
