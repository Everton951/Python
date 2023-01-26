# TUPLAS
n = 7, 5, 3, 1

for c in n:
    print(f'{c}', end='  ')

# OUTRA FORA
for c in range(0, len(n)):
    print(f'{n[c]}')

# PEGAR A POSIÇO DA COMIDA
for pos, c in enumerate(n):
    print(f'Número {c} está na posição {pos}')

# sorted = ORGANIZADO / EM ORDEM
print(sorted(n))

pessoa = ['Gustavo', 39, 'M', 81.5]
print(pessoa)
