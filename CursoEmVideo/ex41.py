# CRIAR UMA TUPLA COM VÁRIAS PALAVRAS (SEM ACENTOS) - MOSTRAR AS VOGAIS
palavras = ['aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro']
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\nPrograma Finalizado !')