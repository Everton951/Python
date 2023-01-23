# LER 4 VALORES E GUARDAR NUMA TUPLA - QUANTAS VEZES APARECE O VALOR 9 - POSIÇÃO DO PRIMEIRO VALOR 3 - QUAIS SÃO OS NÚMEROS PARES
n = [int(input('Digite um número: ')), int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))]
print(f'Você digitou os valores: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
print(f'O valor 3 apareceu na posição {n.index(3) + 1}')