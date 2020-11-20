# Variável float
salario = float(input('Digite o salário do funcionario: '))
# Cores
cor = {'fim': '\033[m',
       'verde': '\033[32m'}
# IFS
if salario > 1250:
    salario = salario * 10/100
else:
    salario = salario * 15/100
# Print
print('O salário novo do funcionario {}{:.2f}{}'.format(cor['verde'], salario, cor['fim']))
