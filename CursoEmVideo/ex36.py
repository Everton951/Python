# NÚMERO POR EXTENSO - DIGITAR UM NÚMERO (INTEIRO) - E FAZER O PROGRAMA DIZER POR EXTENSO
cont = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
while True:
    while True:
        n = int(input('Digite um número entre 0 e 10: '))
        if n <= 10 and n >= 0:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {cont[n]}')
    escolha = str(input('Você quer continuar ? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-' * 30)
print('Programa Finalizado!')