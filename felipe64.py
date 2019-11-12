# Jogo pedra x papel x tesoura TESTE PARA RECORDAR

from time import sleep
from random import randint

sair = 0
while True:

    lista = ("0", "PEDRA", "PAPEL", "TESOURA")
    jogador = int(input("""PEDRA X PAPEL X TESOURA
[1] PEDRA
[2] PAPEL
[3] TESOURA
    Qual é sua jogada? """))

    while jogador > 3:
        print("Opção inválida! Jogue [1], [2] ou [3].")
        jogador = int(input("""PEDRA X PAPEL X TESOURA
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
    Qual é sua jogada? """))

    pc = randint(1, 3)
    print(f"Você jogou {lista[jogador]}, e o computador jogou {lista[pc]}!")
    sleep(1)
    if jogador == pc:
        print("O JOGO EMPATOU!")
    elif jogador == 3 and pc == 2 or jogador == 1 and pc == 3:
        print("VOCÊ GANHOU!")
    else :
        print("VOCÊ PEDEU!")

    sair = str(input("Deseja sair? [S/N] ")).upper().strip()    
    if sair in "S":
        break