n = 1
totPar = totImpar = 0
while n != 0:
    n = int(input('Digite um número ou 0 para sair do programa: '))
    if n % 2 == 0:
        totPar += 1
    else:
        totImpar += 1
    if n == 0:
        totPar -= 1
print(f'Total de Pares: {totPar}')
print(f'Total de Ímpares: {totImpar}')