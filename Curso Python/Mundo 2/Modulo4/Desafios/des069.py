# Variáveis
dmenor = homens = muieDMaior = 0
# While
while True:
    # Variáveis int e string
    idade = int(input('Digite a idade: '))
    sexo = str(input('Você é homem ou mulher? [H/M]').upper())
    # Repetição do sexo
    while True:
        if sexo == 'H' or sexo == 'M':
            break
        else:
            sexo = str(input('Você é homem ou mulher? [H/M]').upper())
    # Repetição da pergunta
    pergunta = str(input('Quer continuar? [S/N]').upper())
    while True:
        if pergunta == 'S' or pergunta == 'N':
            break
        else:
            pergunta = str(input('Quer continuar? [S/N]').upper())
    # Objetivos
    if idade < 18:
        dmenor += 1
    if sexo == 'H':
        homens += 1
    if sexo == 'M' and idade < 20:
        muieDMaior += 1
    # Sair ou entrar
    if pergunta == 'N':
        break
print(f'''No total, existe {dmenor} pessoas menores de 18 anos
No total, a {homens} homens cadastrados
No total, a {muieDMaior} mulheres menores de 20 anos''')
