n = []
maior = menor = 0
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print('-=' * 30)
print(f'Maior valor {maior} nas posições ', end=' ')

print(f'Menor valor {menor} nas posições ', end=' ')