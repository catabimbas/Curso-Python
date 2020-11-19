# Variável
idade = int(input('Digite o ano de nascimento: '))
# Variáveis
classificacao = ['Mirim', 'Infantil', 'Junior', 'Sênior', 'Master']
idade = 2020 - idade
# IFS
if idade < 9:
    print(f"A sua categoria: {classificacao[0]}")
elif 9 < idade <= 14:
    print(f"A sua categoria: {classificacao[1]}")
elif 15 <= idade < 19:
    print(f"A sua categoria: {classificacao[2]}")
elif 19 <= idade < 20:
    print(f"A sua categoria: {classificacao[3]}")
else:
    print(f"A sua categoria: {classificacao[4]}")

