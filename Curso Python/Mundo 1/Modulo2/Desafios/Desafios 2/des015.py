dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
dias = dias * 60
km = km * 0.15
print(f'O proço total a pagar é R${dias + km:.2f}')
