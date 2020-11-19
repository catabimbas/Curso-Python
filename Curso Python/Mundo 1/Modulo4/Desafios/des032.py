salario = float(input('Digite o salário do funcionario: '))
if salario > 1250:
    salariot = salario * 10/100
else:
    salariot = salario * 15/100
print(f'O salário novo do funcionario {salariot}')
