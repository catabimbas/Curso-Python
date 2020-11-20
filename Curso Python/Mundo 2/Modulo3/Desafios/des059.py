# Variáveis int
valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
# Repetição de opções
opcao = 0
while opcao != 5:
    opcao = int(input('''O que você quer fazer com esses valores?
    [1] somar
    [2] multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    Qual Opção você deseja? '''))
    # IFS
    if opcao == 1:
        res = valor_1 + valor_2
        print(f'A soma total é {res}')
    elif opcao == 2:
        res = valor_1 * valor_2
        print(f'A multiplicação total é {res}')
    elif opcao == 3:
        if valor_1 > valor_2:
            print('O primeiro valor é maior')
        else:
            print('O segundo valor é maior')
    elif opcao == 4:
        valor_1 = int(input('Digite o novo número do primeiro valor: '))
        valor_2 = int(input('Digite o novo número do segundo valor: '))
# Print
print('Acabou!')
