from random import randint
pc = randint(0,3)
tentativas = 1
n = int(input('Digite um n�mero entre 0 e 5: '))
if n == pc:
    print(f'Valores iguais. Voc� acertou na primeira jogada.')
else:
    print(f'PC escolheu {pc}. Tente novamente.')
    while pc != n:
        n = int(input('Digite um n�mero entre 0 e 5: '))
        tentativas += 1
print(f'Foram necess�rias {tentativas} jogadas para acertar o mesmo valor.')