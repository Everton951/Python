
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
