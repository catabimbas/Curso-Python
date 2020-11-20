# Variáveis int float
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
ano = int(input('Quantos anos você vai pagar? '))
# Variáveis
anoa = ano * 12
aumento = salario * 30/100
salariopor = salario + aumento
mensal = casa//anoa
# IFS
print(f'Para compra a casa de R${casa:.2f} em {ano} anos a prestação será de R${mensal:.2f}')
if salario >= mensal:
    print('Você poderá fazer o empréstismo')
elif salariopor >= mensal:
    print('Você poderá fazer o empréstismo, mas estará faltando dinheiro')
else:
    print('O empréstimo será negado')
