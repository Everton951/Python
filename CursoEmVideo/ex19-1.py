sexo = str(input('Digite "M" para Masculino e "F" para Feminino: ')).strip().upper()
while sexo not in 'F M':
    print('Tente Novamente')
    sexo = str(input('Digite "M" para Masculino e "F" para Feminino: ')).strip().upper()
print(sexo)