# Variáveis
preco_total = preco_menor = preco_mil = c = 0
nome_menor = ''
# Repetições while
while True:
    # Front
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    # Inseri os primeiros valores
    while c != 1:
        preco_maior = preco_menor = preco
        c += 1
    # Faz a correção caso o vendedor tenha digitado errado
    pergunta = str(input('Que continuar? [S/N]').upper())
    while True:
        if pergunta == 'S' or pergunta == 'N':
            break
        else:
            pergunta = str(input('Que continuar? [S/N]').upper())
    # Back
    # Preco Adicionais
    if preco >= 1000.00:
        preco_mil += 1
    # Preço menor
    preco_total += preco
    if preco_menor > preco:
        preco_menor = preco
        nome_menor = produto
    # Confirmação
    if c == 1 and pergunta == 'N':
        nome_menor = produto
        break
    elif pergunta == 'N':
        break
# Print
print(f'''O Total foi R${preco_total:.2f}
Tem {preco_mil} produtos custando mais de R$1000.00
O produto mais barato foi {nome_menor} que custa R${preco_menor:.2f}''')
