print('Digite M se for homem')
print('Digite F se for mulher')
sexo = str(input('Você é de qual sexo: '))
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Você digitou errado, digite novamente: '))
print('Está certo')
