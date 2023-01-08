i = int(input('A contagem começa de quanto ? '))
f = int(input('A contagem vai até quanto ? '))
p =int(input('A contagem vai pular de quanto em quanto ? '))
for c in range(i, (f + 1), p):
    print(c)
