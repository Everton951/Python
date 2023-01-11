from random import randint
pc = randint(0, 5)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite um número entre 0 e 5: '))
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente mais uma vez.')
        palpite += 1
print(f'Acertou')
print(f'Levou {palpite} palpites.')