n = [int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))]
maior = menor = 0
for pos, c in enumerate(n):
    print(f'Posição {pos + 1} = {c}')
    if c == 1:
        maior = c
        menor = c
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print('-=' * 15)
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')