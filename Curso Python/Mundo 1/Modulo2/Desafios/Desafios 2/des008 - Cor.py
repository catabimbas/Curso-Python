# Variável int
metro = int(input('Digite um valor: '))
# Variáveis
centimetro = metro * 100
milimetros = centimetro * 10
# Cor
cor = {'fim': '\033[m',
       'cinza': '\033[37m'}
# Print
print('{}{}{} metros tem {}{}{} centímetros e {}{}{} metros tem {}{}{} milimetros'.format(cor['cinza'], metro, cor['fim'],
                                                                   cor['cinza'], centimetro, cor['fim'],
                                                                   cor['cinza'], metro,cor['fim'],
                                                                   cor['cinza'], milimetros, cor['fim']))
