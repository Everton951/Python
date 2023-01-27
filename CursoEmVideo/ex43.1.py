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
for pos, valor in enumerate(n):
    if valor == maior:
        print(f'{pos}... ', end=' ')
print()
print(f'Menor valor {menor} nas posições ', end=' ')
for pos, valor in enumerate(n):
    if valor == menor:
        print(f'{pos}... ', end=' ')
print()


numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso ...')
    else:
        print('Valor duplicado. Não vou adicionar.')
    escolha = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Valor Inválido.\nVocê quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('=-' * 30)
print(f'Você digitou os valores: {sorted(numeros)}')
