#digitar números e perguntar se quer continuar - somar - média - total de números - maior e menor valor - 
n = s = m = cont = maior = menor = 0
escolha = ''
while escolha != 'N':
    n = int(input('Digite um número: '))
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()
    cont += 1
    s += n
    print(f'Soma: {s}')
    m = s / cont
    print(f'Média: {m :.1f}')
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Foram digitados {cont} número(s) e a SOMA foi {s}')
print(f'A MÉDIA dos valores foi {m :.1f}')
print(f'o MAIOR valor digitado foi {maior} e o MENOR valor digitado foi {menor}.')