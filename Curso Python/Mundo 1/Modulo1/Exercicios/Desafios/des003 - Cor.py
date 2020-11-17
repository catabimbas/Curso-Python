print('--------Data de Nascimento--------')
# Variáveis
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
# Cor
cor = {'verde': '\033[32m',
       'fim': '\033[m'}
# Print
print('Você nasceu no dia {}{}{} de {}{}{} de {}{}{}'.format(cor['verde'], dia, cor['fim'],
                                                             cor['verde'], mes, cor['fim'],
                                                             cor['verde'], ano, cor['fim']))
