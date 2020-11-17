# Variável
name = input('Digite algo: ')
# Cor
cor = {'fim': '\033[m',
       'branco': '\033[30m'}
# Print
print('O tipo desse valor: {}{}{}'.format(cor['branco'], type(name), cor['fim']))
print('Só tem espaço? {}{}{}'.format(cor['branco'], name.isspace(), cor['fim']))
print('É um número? {}{}{}'.format(cor['branco'], name.isalnum(), cor['fim']))
print('É alfabético? {}{}{}'.format(cor['branco'], name.isalpha(), cor['fim']))
print('É alfanumérico? {}{}{}'.format(cor['branco'], name.isalnum(), cor['fim']))
print('Está em maiúsculas? {}{}{}'.format(cor['branco'], name.isupper(), cor['fim']))
print('Está minúsculas? {}{}{}'.format(cor['branco'], name.islower(), cor['fim']))
print('Está capitalizada? {}{}{}'.format(cor['branco'], name.istitle(), cor['fim']))
