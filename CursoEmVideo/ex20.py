sexo = str(input('Digite "M" para Masculino e "F" para Feminino: ')).strip().upper()
while sexo not in 'M F':
    print('-' * 40)
    print('Valor Inválido. Tente novamente.')
    print('-' * 40)
    sexo = str(input('Digite "M" para Masculino e "F" para Feminino: ')).strip().upper()
print(f'Muito bem.\nSexo: {sexo}')
