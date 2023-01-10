q = int(input('Quantas pessoas você quer verificar ? '))
maior = menor = 0
for c in range(1, (q + 1)):
    peso = float(input(f'Digite o peso número {c}: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')