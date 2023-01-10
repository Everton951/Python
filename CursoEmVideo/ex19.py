# Pegar o nome - Idade - se é masculino ou feminino - maior e menor idade - média de idade - mulheres abaixo de 18 anos - nome do homem mais velho e ,mais jovem- nome da mulher mais nova e mais velha
from datetime import date
maiorIdade = menorIdade = 0
maisVelho = maisJovem = ''
mulherVelha = mulherNova = ''
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
            if sexo == 'M':
                maisVelho = nome
            else:
                mulherVelha = nome
        if idade < menorIdade:
            menorIdade = idade
            maisJovem = nome
            if sexo == 'M':
                maisJovem = nome
            else:
                mulherNova = nome
    if sexo == 'F' and idade < 18:
        MulherMenor += 1
    else:
        MulherMaior += 1
    if sexo == 'M' and idade < 18:
        HomemMenor += 1
    else:
        HomemMaior += 1
print('-' * 30)
print(f'A pessoa mais velho é {maisVelho} com {maiorIdade} anos.')
print(f'A pessoa mais jovem do grupo é {maisJovem} com {menorIdade} anos.')
print(f'Nesse grupo a um total de {totHomem} homem(s) e {totMulher} mulher(es).')
print(f'A média de idade foi {(mediaIdade)/q :.0f} anos.')
print(f'Mulheres menores de idade: {MulherMenor}')
print(f'Mulheres maiores de idade: {MulherMaior}')
print(f'Homens menores de idade: {HomemMenor}')
print(f'Homens maiores de idade: {HomemMaior}')
print(f'A mulher mais velha é {mulherVelha}')
print(f'A mulher mais nova é {mulherNova}')
print(f'O homem mais velho é {maisVelho}')
print(f'O homem mais jovem é {maisJovem}')
