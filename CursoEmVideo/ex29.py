'''from math import factorial
n = int(input('Digite o fatorial que você quer: '))
f = factorial(n)
print(f)'''

n = int(input('Digite o Fatorial que você quer: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f)
