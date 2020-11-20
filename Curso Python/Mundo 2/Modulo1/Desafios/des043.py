peso = float(input('Qual o seu peso atual? '))
altura = float(input('Qual a sua altura atual? '))
IMC = peso / (altura * altura)
if IMC < 18.5:
    print("Você está abaixo do peso")
elif 18.5 < IMC < 25:
    print('Você está no peso ideal')
elif 25 < IMC < 30:
    print('Você está Sobrepeso')
elif 30 < IMC < 40:
    print('Você esta na Obesidade')
else:
    print('Obesidade mórbida')

