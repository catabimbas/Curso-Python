# Variável int
num = int(input('Digite um número: '))
# Variável
analisa_primo = 0
# Repetição
for c in range(1,num+1):
    print(c, end=' ')
    # IF
    if num % c == 0:
        analisa_primo += 1
# Print
print(f'\nO número {num} foi dividido {analisa_primo} vezes')
if analisa_primo <= 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')
