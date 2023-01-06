preco = float(input('Digite o preço do produto: '))
formaPag = str(input('Digite a forma de pagamento.\n'
                     '[ Dinheiro / Cheque / Cartão / 2x no cartão /'
                     ' 3x ou mais no cartão]: ')).strip().lower()
if formaPag in 'dinheiro cheque':
    desc = preco * 0.1
    novoPreco = preco - desc
    print(f'Preço a ser pago com desconto de 10%: R${novoPreco :.2f} reias.')
elif formaPag == 'cartão' or formaPag == 'cartao':
    desc = preco * 0.05
    novoPreco = preco - desc
    print(f'Preço a ser pago com desconto de 5%: R${novoPreco :.2f} reais.')
elif formaPag == '2x':
    print(f'Preço normal sem desconto: R${preco :.2f} reais.')
elif formaPag == '3x':
    aum = preco * 0.3
    novoPreco = preco + aum
    print(f'Com um aumento de 30%, o novo preço é R${novoPreco :.2f} reais.')
else:
    print('VALOR INVÁLIDO')
