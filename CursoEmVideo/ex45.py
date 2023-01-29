valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'Voc� digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescentes s�o {valores}')
if 5 in valores:
    print('O 5 faz parte da lista.')
else:
    print('O valor 5 n�o foi encontrado na lista.')
