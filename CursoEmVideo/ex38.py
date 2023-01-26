# GERAR 5 NÚMEROS ALEATÓRIOS E COLOCAR NUMA TUPLA - MOSTRAR TODOS OS VALORES - MOSTRAR MAIOR E O MENOR VALOR
from random import randint
n = [randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)]
for c in n:
    print(c, end=' ')
print(f'\nO maior valor foi: {max(n)}')
print(f'O menor valor foi: {min(n)}')
