# caixa eletrônico - perguntar quanto quer sacar (inteiro) - o programa informa quantas cédulas de cada valor serão entregues - R$ 50 - 20 - 10 e 1
n = int(input('Quanto você quer sacar: '))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de {ced} reais.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
