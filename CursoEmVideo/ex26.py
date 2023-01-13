#dizer quantos números foi digitado - soma deles - maior e menor valor - 999 para sair
n = cont = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'Foi digitado {cont} número(s).')
print(f'Soma: {s}')
print(f'Maior valor: {maior}\nMenor valor: {menor}.')
