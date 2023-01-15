#jogo de par ou impar - perguntar se quer par ou impar - contar quantas vezes você venceu - so parar quando você perder o jogo
from random import randint
s = cont = 0
while True:
    pc = randint(0, 10)
    print('=-' * 30)
    print('Jogo do PAR ou ÍMPAR')
    n = int(input('Digite um valor: '))
    s = pc + n
    escolha = str(input('Você quer PAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
    while escolha not in 'PI':
        print('Valor Inválido. Tente novamente')
        escolha = str(input('Você quer PAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
        print(escolha)
    if s % 2 == 0:
        print(f'Você jogou {n} e o PC {pc}. Total de {s}, deu PAR')
        if escolha == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente.')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print(f'Você jogou {n} e o PC {pc}. Total de {s}, deu ÍMPAR')
        if escolha == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente.')
            cont += 1
        else:
            print('Você PERDEU!')            
            break
print('=-' * 30)
print('GAME OVER! você venceu {cont} vezes.')