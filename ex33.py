# ler o nome do produto e seu preço - perguntar se quer continuar ou não - total da compra - quantos curstam mais de 1000 - nome do produto mais barato
escolha = ''
total = Maiosde1000 = ProdutoBarato = 0
while escolha != 'N':
    produto = str(input('Qual o nome do produto: ')).strip()
    preco = float(input(f'Preço do {produto.capitalize()}: '))
    escolha = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    while escolha not in 'S N':
        print('Valor Inválido. Tente novamente.')
        escolha = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    