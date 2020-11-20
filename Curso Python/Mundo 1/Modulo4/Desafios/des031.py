kmviagem = int(input('Quantos Km tem a viagem? '))
if kmviagem < 200:
    passagem = kmviagem * 0.50
else:
    passagem = kmviagem * 0.45
print('O preço do seu voo fica por {}'.format(passagem))
