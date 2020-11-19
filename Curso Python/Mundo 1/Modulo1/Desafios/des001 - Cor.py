nome = input('Qual é o seu nome? ')
cor = {'ciano': '\033[36m',
       'fim': '\033[m'}
print('Seja Bem-vindo {}{}{}'.format(cor['ciano'], nome, cor['fim']))
