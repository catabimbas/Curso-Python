# Variável string
polindromo = str(input('Digite uma frase: '))
# Variáveis
palavras = polindromo.split()
junto = ''.join(polindromo)
inverso = ''
# Repetição
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
# IF
if inverso.capitalize() != junto.capitalize():
    print('Ele não é polindromo')
else:
    print('Ele é polindromo')
