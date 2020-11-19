cidade = str(input('Digite o nome da sua cidade: '))
cidadenome = cidade.split()
print(f'A cidade começa com santo? {"SANTO" in cidadenome[0].upper()}')
