s = 0
for c in range(0, 500):
    if c % 3 == 0:
        if c != 0:
            s += c
print(s)

#41583


s = 0
cont = 0
for c in range(0, 501):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'Soma: {s}')
print(f'Foram somados {cont} números.')
