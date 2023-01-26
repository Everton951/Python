'''n = [1, 2, 3, 4, 5]
n.append(7) # ADICIONAR O VALOR 7
del n[2] #ELIMINAR O NÚMERO 3
#n.pop[3] #ELIMINAR O NÚMERO 3
#n.pop() #ELIMINA O ÚLTIMO VALOR DA LISTA
#n.remove(3) #ELIMINAR O NÚMERO 3
n[3] = 10
n.insert(2, 0) # INSERIR NA POSIÇÃO 2 O VALOR 0
valores = list(range(0, 11)) # CRIA UMA LISTA COM OS VALORES DE 0 ATÉ 10
for c in n:
    print(c, end='  ')
print()'''

valores = []
valores.append(5)
valores.append(4)
valores.append(7)

for pos, c in enumerate(valores):
    print(f'Na posição {pos + 1} encontrei o valor {c}')
print('FIM!')