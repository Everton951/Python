tot = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print(f'Divisivel por: {c}')
        tot += 1
    else:
        print(f'Não é divisivel por {c}')
print(f'O número {n} foi divisivel {tot} vezes.')
if tot == 2:
    print(f'{n} é um número PRIMo')
else:
    print(f'{n} não é um número PRIMO.')
