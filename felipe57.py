def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)

for c in range(0,2):
    escreva(str(input('Escreva algo: ')))    