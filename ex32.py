from datetime import date
ano = date.today().year
while True:
    nasc = int(input('Ano de nascimento: '))
    idade = ano - nasc
    sexo = str(input('Qual seu sexo ? [M/F]: ')).strip().upper()[0]
    while sexo not in 'M F':
        print('Valor Inválido. Tente novamente.')
        sexo = str(input('Qual seu sexo ? [M/F]: ')).strip().upper()[0]
    