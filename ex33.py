# ler o nome do produto e seu preço - perguntar se quer continuar ou não - total da compra - quantos curstam mais de 1000 - nome do produto mais barato - nome do produto mais caro
escolha = nome = ''
total = Maiosde1000 = ProdutoBarato = Produtocaro = 0
cont = 1
while escolha != 'N':
    produto = str(input('Qual o nome do produto: ')).strip()
    preco = float(input(f'Preço do {produto.capitalize()}: '))
    escolha = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    while escolha not in 'S N':
        print('Valor Inválido. Tente novamente.')
        escolha = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if preco >= 1000:
        Maiosde1000 += 1
    if cont == 1:
        ProdutoBarato = preco
        nome = produto
    else:
        if preco < ProdutoBarato:
            ProdutoBarato = preco
            nome = produto
    if cont == 1:
        Produtocaro = preco
        nome = produto
    else:
        if preco > Produtocaro:
            Produtocaro = preco
            nome = produto
    cont += 1
print('-' * 30)
if Maiosde1000 >= 1:        
    print(f'Tem {Maiosde1000} produto(s) acima de 1000 reais.')
else:
    print(f'Não há nenhum produto acima de 1000 reais.')
print(f'O produto mais barato é o {nome.capitalize()} e custa {ProdutoBarato :.2f} reais.')
print(f'O produto mais caro é o {nome.capitalize()} e custa {Produtocaro :.2f} reais.')
