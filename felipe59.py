from time import sleep


def maior(* números):
    maior = cont = 0
    for c in números:
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = c
        elif c > maior:
            maior = c
        cont += 1      
    print(f'Foram informados {cont} valores, e o maior é {maior}.')


maior(1, 3, 50, 7,56, 13)      
maior()
maior(1, 2)
maior(-1, -20)
maior(300, 300)          