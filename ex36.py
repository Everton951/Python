# NÚMERO POR EXTENSO - DIGITAR UM NÚMERO (INTEIRO) - E FAZER O PROGRAMA DIZER POR EXTENSO
cont = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'novo', 'dez']
while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if n <= 10 and n >= 0:
        break
    print(' Tente novamente.', end='')