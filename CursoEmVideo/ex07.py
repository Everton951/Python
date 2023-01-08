n = int(input('Quantas vezes você quer somar ? '))
s = 0
sTotal = 0
for c in range(0, n):
    num = int(input('Digite o primeiro número que quer somar: '))
    num2 = int(input('Digite o segundo número que quer somar: '))
    s = num + num2
    sTotal += s
    print(f'Soma do número {c +1}: {s}')
    s = 0
print(f'Soma Total dos valores: {sTotal}')
