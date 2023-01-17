## idade - sexo - quer continuar - quantos homens e mulheres - mulheres com mais de 18 anos - quantas pessoas com mais de 18 anos
from datetime import date
ano = date.today().year
totHom = totMul = MulherMaior = totMaiores = 0
while True:
    nasc = int(input('Ano de nascimento: '))
    idade = ano - nasc
    sexo = str(input('Qual seu sexo ? [M/F]: ')).strip().upper()[0]
    while sexo not in 'M F':
        print('Valor Inválido. Tente novamente.')
        sexo = str(input('Qual seu sexo ? [M/F]: ')).strip().upper()[0]
    escolha = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    while escolha not in 'S N':
        print('Valor Inválido. Tente novamente.')
        escolha = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
    