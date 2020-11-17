# Usando IF e ELSE Números e IFS simplificados
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(s))
print('PARABÉNS!' if s >= 6 else 'ESTUDE MAIS!')
----------------------------------------
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = (n1 + n2)/2
if s >= 6.0:
    print('A média foi de {}, Aprovado'.format(s))
else:
    print('A média foi de {}, Reprovado'.format(s))
"""
# Usando IF e ELSE String
"""
nome = str(input('Qual o seu nome? '))
if nome == 'Pedro':
    print('Pedro Filha da puta, devolve o macaco')
    print('Bom dia é o caralho')
else:
    print('Agradeça pelo seu nome não ser Pedro')
    print('Bom dia, {}'.format(nome))
----------------------------------------
nome = str(input('Qual é o seu nome? '))
if nome == 'Pedro':
    print('Pedro Filha da puta, devolve o macaco')
else:
    print('Agradeça pelo seu nome não ser Pedro')
print('Bom dia: {}'.format(nome))
"""
# Usando IF String
"""
nome = str(input('Qual é o seu nome? '))
if nome == 'Pedro':
    print('Pedro Filha da puta, devolve o macaco')
print('Bom dia {}'.format(nome))
"""