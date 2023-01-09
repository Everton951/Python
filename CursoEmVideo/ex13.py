#somar pares e ímpares e mostrar quantos pares e quantos ímpares
sPar = 0
parTotal = 0
sImpar = 0
imparTot = 0
n = int(input('Quantas vezes você quer somar ? '))
for c in range(1, (n+1)):
    if c % 2 == 0:
        sPar += c
        parTotal += 1
    else:
        sImpar += c
        imparTot += 1
print(f'Soma dos Pares: {sPar}')
print(f'Total de Pares somados: {parTotal}')
print(f'Soma dos Ímpares: {sImpar}')
print(f'Total de Ímpares somados: {imparTot}')
