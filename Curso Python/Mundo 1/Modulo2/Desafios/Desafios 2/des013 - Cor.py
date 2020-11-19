funcionario = float(input('Quantos reais esse funcíonário ganhava? '))
# Variáveis
aumento = funcionario * 15 / 100
salario_novo = funcionario + aumento
# Cores
cor = {'fim': '\033[m',
       'verde': '\033[32m'}
# Print
print('O novo salário atual é de {}{:.2f}{}'.format(cor['verde'], salario_novo, cor['fim']))
