from datetime import date
ano = date.today().year
maior = menor = 0
idadeMaior = idadeMenor = 0
q = int(input('Quantas vezes voc� quer verificar ? '))
for c in range(1,(q + 1)):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
    if c == 1:
        idadeMaior = idade
        idadeMenor = idade
    else:
        if idade > idadeMaior:
            idadeMaior = idade
        if idade < idadeMenor:
            idadeMenor = idade
print(f'Maiores de idade: {maior}')
print(f'Menores de idade: {menor}')
print(f'Maior idade: {idadeMaior} anos.')
print(f'Menor idade: {idadeMenor} anos.')