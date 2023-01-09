from datetime import date
ano = date.today().year
maior = menor = 0
q = int(input('Quantas vezes você quer verificar ? '))
for c in range(1, (q + 1)):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = ano - nasc
    maiorIdade = idade
    menorIdade = idade
    if idade >= 18:
        maior += 1
    else:
        menor += 1
    
    if idade > maiorIdade:
        maiorIdade = idade
    if idade < menorIdade:
        menorIdade = idade
print(f'Foram verificados {q} vezes.')
print(f'São maiores de idade: {maior}')
print(f'São menores de idade: {menor}')
print(f'A maior idade foi: {maiorIdade}')
print(f'A menor idade foi: {menorIdade}')