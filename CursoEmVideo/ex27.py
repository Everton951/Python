#tabuada - número negativo para sair

while True:
    n = int(input('Qual tabuada você quer ? [Número negativo para SAIR]'))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')