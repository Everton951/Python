from datetime import date
ano = date.today().year
maior = menor = 0
q = int(input('Quantas vezes você quer verificar ? '))
for c in range(1, (q + 1)):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Foram verificados {q} vezes.')
print(f'São maiores de idade: {maior}')
print(f'São menores de idade: {menor}')