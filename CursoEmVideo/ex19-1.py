from datetime import date
maiorIdadeHomem = menorIdadeMulher = 0
totMulher = totIdade = 0
nomeVelho = ''
nomeNova = ''
q = int(input('Quantas pessoas você quer verificar ? '))
ano = date.today().year
for c in range(1, (q + 1)):
    nome = str(input('Digite o nome da pessoa: ')).strip().capitalize()
    nasc = int(input('Digite o ano de nascimento: '))
    idade = ano - nasc
    sexo = str(input('Digite "M" para Masculino e "F" para Feminino: ')).strip().upper()
    while sexo not in 'M F':
        print('Valor inválido. Tente novamente.')
        sexo = str(input('Digite "M" para Masculino e "F" para Feminino: ')).strip().upper()
    if c == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    totIdade += idade
    if sexo == 'F' and idade <= 18:
        totMulher += 1
    if c == 1 and sexo == 'F':
        menorIdadeMulher = idade
        nomeNova = nome
    if idade < menorIdadeMulher:
        menorIdadeMulher = idade
        nomeNova = nome
    print('-' * 40)
mediaIdade = totIdade / q
print(f'Média de idade(s): {mediaIdade}')
print(f'Mulheres menores de idade: {totMulher}')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}')
print(f'A mulher mais nova tem {menorIdadeMulher} anos e se chama {nomeNova}')
