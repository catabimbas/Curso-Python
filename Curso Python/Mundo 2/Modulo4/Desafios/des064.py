n = r = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    r += n
print(f'A soma dos valores digitados é {r}')
