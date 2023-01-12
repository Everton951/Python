escolha = 1
maiorValor = menorValor = 0
while escolha != 000:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('''O que você quer fazer:
    [ 1 ] SOMAR
    [ 2 ] SUBTRAIR
    [ 3 ] MULTIPLICAR
    [ 4 ] DIVIDIR
    [ 5 ] MAIOR VALOR
    [ 6 ] MENOR VALOR
    [ 000 ] SAIR DO PROGRAMA''')
    escolha = int(input('Qual a sua escolha? '))
    while escolha > 6 or escolha < 0:
        print('Tente novamente.')
        escolha = int(input('Qual a sua escolha? '))
    if escolha == 1:
        print(f'Soma: {n1 + n2}')
    elif escolha == 2:
        print(f'Subtração: {n1 - n2}')
    elif escolha == 3:
        print(f'Multiplicação: {n1 * n2}')
    elif escolha == 4:
        print(f'Divisão: {n1 / n2}')
    elif escolha == 5:
        if n1 > n2:
            maiorValor = n1
        else:
            maiorValor = n2
        print(f'Maior Valor: {maiorValor}')
    elif escolha == 6:
        if n1 < n2:
            menorValor = n1
        else:
            menorValor = n2
        print(f'Menor Valor: {menorValor}')
    escolha2 = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if escolha2 == 'N':
        break
print('Programa FINALIZADO.')