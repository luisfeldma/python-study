palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR')
for item in palavras:
    print(f'\nNa palara {item} temos as vogais: ', end = '')
    for letra in item:
        if letra in 'AEIOU':
            print(letra, end = '')
a = [1,2,3]
b = a[:]
b[1] = 3
print(f'\n{a}{b}')