from random import randint
from time import sleep
pc = randint(1, 3)
print('Opções: ')
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Qual número você escolhe ? '))
sleep(1)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
if jogador <= 0 or jogador > 3:
    print('Valor INVÁLIDO. Tente novamente!')
elif jogador == pc:
        print('Valores IGUAIS. Jogue novamente !')
elif pc == 1 and jogador == 3:
    print(f'O PC VENCEU!\nPedra ganha de Tesoura')
elif pc == 2 and jogador == 1:
    print(f'O PC VENCEU!\\nPapel ganha de Pedra')
elif pc == 3 and jogador == 2:
    print(f'O PC VENCEU!\nTesoura ganha de Papel')
elif jogador == 1 and pc == 3:
    print(f'O Jogador VENCEU!\nPedra ganha de Tesoura')
elif jogador == 2 and pc == 1:
    print(f'O Jogador VENCEU!\\nPapel ganha de Pedra')
elif jogador == 3 and pc == 2:
    print(f'O Jogador VENCEU!\nTesoura ganha de Papel')