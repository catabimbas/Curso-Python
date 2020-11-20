# Variável int
dataNascimento = int(input('Informe o ano de nascimento: '))
# Variáveis
dataNascimentop = 2020 - dataNascimento
vaiAlista = "Não"
temQueAlista = "Não"
passouAlista = "Não"
# IFS Print
if dataNascimentop < 18:
    vaiAlista = "Sim"
    print('Você vai se alista em {}'.format(dataNascimento + 18))
if dataNascimentop == 18:
    temQueAlista = "Sim"
    print('Você vai poder se alista esse ano')
if dataNascimentop > 18:
    passouAlista = "Sim"
    print('Você deveria ser alistado a {} atrás'.format(dataNascimento-18))
# Prints
print(f"Tu ainda vai se alista? {vaiAlista}")
print(f"Tá na hora de se alista? {temQueAlista}")
print(f"Já passou no tempo de se alista? {passouAlista}")
