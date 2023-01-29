num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
for pos, valor in enumerate(num):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'A lista completa: {num}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
