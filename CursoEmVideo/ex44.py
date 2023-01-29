lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Adicionado ao final da lista...')
    elif n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem: {lista}')

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
