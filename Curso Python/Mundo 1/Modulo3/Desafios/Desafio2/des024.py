# Digitar a Frase
digito = str(input('Digite uma frase: '))
# Variáveis
txtContar = digito.upper().count('A')
txtProcI = digito.upper().find('A')
txtProcF = digito.upper().rfind(max('A'))
# Prints Altamente Formatadas
print(f"Você usou {txtContar} vezes a letra A")
print(f"A primeira vez que aparece a letra (A): {txtProcI}")
print(f"A última vez que aparece a letra (A): {txtProcF}")
