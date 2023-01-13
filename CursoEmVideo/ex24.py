n = cont = s = 0
while n != 999:
    n = int(input('Digite um número: [999 para SAIR]: '))
    if n == 999:
        break
    cont += 1
    s += n
    print(f'Soma: {s}')
print(f'Você digitou {cont} número(s) e a soma foi {s}.')
