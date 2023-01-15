#jogo de par ou impar - perguntar se quer par ou impar - contar quantas vezes você venceu - so parar quando você perder o jogo
from random import randint
s = 0
while True:
    pc = randint(0, 10)
    print('Jogo do PAR ou ÍMPAR')
    n = int(input('Digite um valor: '))
    s = pc + n
    escolha = str(input('Você quer PAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
    while escolha not in 'PI':
        print('Valor Inválido. Tente novamente')
        escolha = str(input('Você quer PAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
        print(escolha)
    print('Programa Finalizado.')
