expr = str(input('Digite uma expressão: '))
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
