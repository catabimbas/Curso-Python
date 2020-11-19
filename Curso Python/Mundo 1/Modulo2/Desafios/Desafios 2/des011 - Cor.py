# Variáveis float
altura = float(input('Quantos metros de altura tem a parede? '))
largura = float(input('Quantos metros de largura tem a parede? '))
# Variáveis
metrosQ = altura * largura
tinta = altura * largura / 2
# Cores
cor = {'fim': '\033[m',
       'branco': '\033[30m',
       'azul': '\033[34m'}
# Print
print('No total, a parede tem {}{}m²{} então serão necessário {}{}{} litros de tinta'.format(cor['branco'], metrosQ, cor['fim'],
                                                                                             cor['azul'], tinta, cor['fim']))
