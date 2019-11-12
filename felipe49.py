from random import randint
lista = []
jogos = []
cont = 0
quant = int(input('Quantas vezes você quer sortear o jogo? '))
tot = 1
while tot <= quant:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])   
    lista.clear()
    tot += 1     
print(jogos)        
#NAO ENTENDI O PROBLEMA COMPLETAMENTE... TERMINAR MAIS TARDE
