# Variáveis int
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
# Variável
media = nota1 / nota2
# IFS Print
if media > 5.0:
    print('Reprovado')
elif 6.9 > media > 5.0:
    print('Recuperação')
else:
    print('Aprovado')
