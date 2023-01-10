# Pegar o nome - Idade - se é masculino ou feminino - maior e menor idade - média de idade - mulheres abaixo de 20 anos - nome do homem mais velho - nome da mulher mais nova
from datetime import date
maiorIdade = menorIdade = 0
maisVelho = ''
maisJovem = ''
totMulher = totHomem = MulherMenor = MulherMaior = HomemMaior = HomemMenor = 0
mediaIdade = 0
q = int(input('Quantas vezes você quer verificar ? '))
ano = date.today().year
for c in range(1, (q + 1)):
    nome = str(input('Digite o nome: ')).strip()
    nasc = int(input('Digite o ano de nascimento: '))
    idade = ano - nasc
    mediaIdade += idade
    sexo = str(input('Digite "M" para Masculino e "F" para Feminino: ')).strip().upper()
    while sexo not in 'F M':
        print('Tente Novamente')
        sexo = str(input('Digite "M" para Masculino e "F" para Feminino: ')).strip().upper()
    if sexo == 'M':
        totHomem += 1
    else:
        totMulher += 1
    if c == 1:
        maiorIdade = idade
        menorIdade = idade
        maisVelho = nome
        maisJovem = nome
    else:
        if idade > maiorIdade:
            maiorIdade = idade
            maisVelho = nome
        if idade < menorIdade:
            menorIdade = idade
            maisJovem = nome
    if sexo == 'F' and idade < 18:
        MulherMenor += 1
    else:
        MulherMaior += 1
print(f'A pessoa mais velho é {maisVelho} com {maiorIdade} anos.')
print(f'A pessoa mais jovem do grupo é {maisJovem} com {menorIdade} anos.')
print(f'Nesse grupo a um total de {totHomem} homem(s) e {totMulher} mulher(es).')
print(f'A média de idade foi {(mediaIdade)/q :.0f} anos.')
print(f'Mulheres menores de idade: {MulherMenor}')
print(f'Homens menores de idade: {HomemMenor}')