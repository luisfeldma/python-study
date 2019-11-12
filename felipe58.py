from time import sleep


def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
        
    print('Contagem de {} a {} de {} em {}: '.format(início, fim, passo, passo))

    if fim > início:
        cont = início
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            cont += passo
            sleep(0.5)
        print('FIM.')
    else:
        cont = início
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            cont -= passo
            sleep(0.5)
        print('FIM.')

 
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a função: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)




