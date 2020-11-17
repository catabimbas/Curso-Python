produto_valor_antigo = int(input('Qual o preço do produto: '))
opcoes = int(input("""----------------------
1 - À Vista (10% de desconto)
2 - No Cartão (5% de desconto)
3 - 2x no Cartão (Preço Normal)
4 - 3x no Cartão (20% de Juros)
----------------------
Qual das opções o produto vai ser pago: """))
if opcoes == 1:
    desconto = produto_valor_antigo * 10/100
    produto_desconto = produto_valor_antigo - desconto
    print(f"O valor do seu produto à vista: {produto_desconto}")
elif opcoes == 2:
    desconto = produto_valor_antigo * 5/100
    produto_desconto = produto_valor_antigo - desconto
    print(f"O valor do seu produto no cartão: {produto_desconto}")
elif opcoes == 3:
    print(f"O valor do seu produto no 2x no cartão: {produto_valor_antigo}")
elif opcoes == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = produto_valor_antigo * 20/100
    produto_juros = produto_valor_antigo + juros
    produto_parcela = produto_juros / parcela
    print(f"O seu produto ficará parcelado em {parcela}x de R${produto_parcela} com juros")
    print(f'Sua compra de R${produto_valor_antigo} vai ficar em R${produto_juros}')
else:
    print('Não existe essa opção ou não foi cadastrada')
