# LISTA DE PREÇOS COM TUPLAS
listagem = ['Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.90, 'Mochila', 120.30, 'Canetas', 22.30, 'Livro', 34.90]
for contador in range(0, len(listagem)):
    if contador % 2 == 0:
        print(f'{listagem[contador]:.<30}', end='')
    else:
        print(f'{listagem[contador]:>7}')