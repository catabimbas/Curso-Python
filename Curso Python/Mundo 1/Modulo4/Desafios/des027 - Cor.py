# Variável int
velocidade = int(input('Qual velocidade o carro percorreu: '))
# Cores
cor = {'fim': '\033[m',
       'amarelo': '\033[33m',
       'vermelho': '\033[31m',
       'verde': '\033[32m'}

# IFS
if velocidade > 80:
    # Váriavel
    precoMulta = (velocidade - 80) * 7
    # Print
    print(f'{cor["vermelho"]}O carro está Multado{cor["fim"]}')
    print(f'{cor["vermelho"]}Ele pagará {cor["amarelo"]}{precoMulta} reais {cor["fim"]}{cor["vermelho"]}na multa{cor["fim"]}')
else:
    # Print
    print(f'{cor["verde"]}Não ultrassou a velocidade máxima{cor["fim"]}')
