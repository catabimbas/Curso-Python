nome_homem = ''
idade_velho = 0
idade_media = 0
idade_novo = 0
for c in range(1, 5):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Homem ou mulher: '.capitalize()))
    idade_novo = idade
    idade_media += idade
    if idade_velho < idade and sexo == 'Homem':
        idade_velho = idade
        nome_homem = nome
    if idade < 20 and sexo == 'Mulher':
        idade_novo += 1
idade_media = idade_media / 4
print(f'''A idade média do grupo é de {idade_media}
O {nome_homem} é o homem mais velho e tem {idade_velho}
No total, existem {idade_novo} menores de 20 anos''')
