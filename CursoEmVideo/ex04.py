import random
jogador = str(input('Escolha entre Pedra / Papel  e Tesoura: ')).strip().lower()
jogo = ['pedra', 'papel', 'tesoura']
pc = random.choice(jogo)
print(pc)
if pc == jogador:
    print(f'Empate.\nTodo mundo escolheu {jogador.capitalize()}')
elif pc == 'pedra' and jogador == 'tesoura':
    print('O PC VENCEU !')
    print(f'{pc} ganha de {jogador}')
elif pc == 'papel' and jogador == 'pedra':
    print('O PC VENCEU !')
    print(f'{pc} ganha de {jogador}')
elif pc == 'tesoura' and jogador == 'papel':
    print('O PC VENCEU !')
    print(f'{pc} ganha de {jogador}')
elif jogador == 'pedra' and pc == 'tesoura':
    print('Você VENCEU !')
    print(f'{jogador} ganha de {pc}')
elif jogador == 'papel' and pc == 'pedra':
    print('Você VENCEU !')
    print(f'{jogador} ganha de {pc}')
elif jogador == 'tesoura' and pc == 'papel':
    print('Você VENCEU !')
    print(f'{jogador} ganha de {pc}')
else:
    print('Valores INVÁLIDOS. Jogue novamente.')
