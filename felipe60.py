from time import sleep
from random import randint


lista = list()
def sorteia(lista):
    """
    Essa função sorteia 5 números aleatórios de 0 a 10.
    Criada por Luis Felipe Miranda
    """
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print('SORTEANDO OS NÚMEROS...')    
    for c in lista:
        print(f'{c} ', end='', flush=True)
        sleep(0.5) 
    print('PRONTO!')  
    sleep(1)


def somaPar(lista):
    listapar = list()
    for c in lista:
        if c % 2 == 0:
            listapar.append(c)
    print(f'A soma dos termos pares dessa lista é {sum(listapar)}')        
    


sorteia(lista)
somaPar(lista)
help(sorteia)
