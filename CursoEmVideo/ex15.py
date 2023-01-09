frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print('É um PALINDROMO')
else:
    print('Não é um palindromo')
