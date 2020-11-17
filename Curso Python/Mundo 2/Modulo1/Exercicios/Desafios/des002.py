# Variável int
num = int(input('Digite um número inteiro: '))
# Opções
opcoes = int(input("""Escolha uma das bases para conversão
[ 1 ] Converter para Binário 
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
Sua Opção: """))
# IFS Opções
if opcoes == 1:
    print('{} Convertido pra binário é igual a: {}'.format(num, bin(num)))
elif opcoes == 2:
    print('{} Convertido para OCTAL é igual a: {}'.format(num, oct(num)))
elif opcoes == 3:
    print('{} Convertido para Hexadecimal é igual a: {}'.format(num, hex(num)))
else:
    print('Essa opção não existe')
