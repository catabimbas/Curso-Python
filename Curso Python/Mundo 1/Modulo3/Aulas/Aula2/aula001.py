# Juntador
"""
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(''.join(frase))
"""
# Divisor split
"""
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])
-------------------------------
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase.split())
"""

# Condicionador in
"""
frase = 'Curso em Vídeo Python'
print('Curso' in frase)
"""
# Substituidor replace
"""
frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
"""
# Analisador find
"""
frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase.find('vídeo'))
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase.find('Vídeo'))
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase.find('Curso'))
"""
# Analisador len e strip
"""
frase = '   Curso em Vídeo Python   '
frase.strip()
print(len(frase))
-------------------------------
frase = '   Curso em Vídeo Python   '
print(len(frase))
-------------------------------
frase = 'Curso em Vídeo Python'
print(len(frase))
"""
# Analisador count
"""
frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase.count('o'))
"""
# Dica massa do professor
"""
print('''Welcome! Are you completely new to programming
If not then we presume tou will be looking for information
about why and how to get started with Python. Fortunately
an experienced programmer in my programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!''')
"""
# Formas de usar o Fatiamento
"""
frase = 'Curso em Vídeo Python'
print(frase[::2])
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase[1::2])
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase[1:15:2])
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase[13:])
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase[:13])
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase[3:13])
-------------------------------
frase = 'Curso em Vídeo Python'
print(frase[3])
"""