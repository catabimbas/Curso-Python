# Variáveis
maiores = 0
menores = 0
# Repetição
for c in range(1,8):
    ano_Nascimento = int(input('Digite o ano de nascimento: '))
    ano_Nascimento = 2020 - ano_Nascimento
    # IF
    if ano_Nascimento > 21:
        maiores += 1
    else:
        menores += 1
# Print
print(f'''{maiores} pessoas não tem a idade de amadurecimento
{menores} pessoas já são maiores''')