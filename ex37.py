cont = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if n <= 20 and n >= 0:
            break
        print(f'Tente novamente. ', end='')
    print(f'Você digitou o número {cont[n]}')
    escolha = str(input('Você quer continuar ? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('Programa Finalizado!')