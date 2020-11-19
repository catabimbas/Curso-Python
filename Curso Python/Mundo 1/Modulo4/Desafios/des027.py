velocidade = int(input('Qual velocidade o carro percorreu: '))
if velocidade > 80:
    # Váriavel
    precoMulta = (velocidade - 80) * 7
    # Print
    print('O carro está Multado')
    print('Ele pagará {} reais na multa'.format(precoMulta))
else:
    print('Não ultrassou a velocidade máxima')
