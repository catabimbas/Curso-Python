from random import sample
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = sample(lista, 4)
print('Os sorteados para apresentarem os trabalhos \n{}: Primeiro \n{}: Segundo \n{}: Terceiro\n{}: Quarto'.format(escolhido[0], escolhido[1], escolhido[2], escolhido[3]))
