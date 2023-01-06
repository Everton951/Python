preco = float(input('Digite o preço do produto: '))
print("""Quantas parcelas você quer dividir ?
[ 1 ] A vista Dinheiro ou Cheque
[ 2 ] A vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
escolha = int(input('Escolha a forma de pagamento: '))
if escolha <= 0 or escolha > 4:
    print('-' * 35)
    print('Valores INVÁLIDOS. Tente novamente')
    print('-' * 35)
else:
    if escolha == 1:
        desc = preco * 0.1
        novoPreco = preco - desc
        print(f'Com 10% de desconto, a compra sai no valor de R${novoPreco :.2f} reais.')
    elif escolha == 2:
        desc = preco * 0.05
        novoPreco = preco - desc
        print(f'Com o desconto de 5%, o novo preço do produto sai a R${novoPreco :.2f} reais.')
    elif escolha == 3:
        prestacao = preco / 2
        print(f'Dividido 2 vezes no cartão, a prestação do produto sai a R${prestacao :.2f} reais.')
    else:
        aum = preco * 0.2
        novoPreco = preco + aum
        div = int(input('Quantas vezes você quer dividir ? '))
        prestacao = novoPreco / div
        print(f'Com 20% de aumento, o novo preço produto vai ser R${novoPreco :.2f} reais, com prestações a R${prestacao :.2f} reais.')
