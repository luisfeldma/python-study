from random import randint
itens = ("PEDRA", "PAPEL", "TESOURA")
print("Vamos jogar jokenpô?")
print("""Escolha:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input("Qual você escolhe? "))
pc = randint(0, 2)
print("==" * 14)
print("Você escolheu {}!".format(itens[jogador]))
print("O computador escolheu {}!".format(itens[pc]))
print("==" * 14)   
if pc == 0:
    if jogador == 0:
        print("JOGO EMPATADO!")
    elif jogador == 1:
        print("VOCÊ GANHOU!")
    elif jogador == 2:
        print("VOCÊ PERDEU!")
    else: 
        print("JOGADA INVÁLIDA!!!")            
elif pc == 1:
    if jogador == 0:
        print("VOCÊ PERDEU!")
    elif jogador == 1:
        print("JOGO EMPATADO!")
    elif jogador == 2:
        print("VOCÊ GANHOU!")
    else: 
        print("JOGADA INVÁLIDA!!!")
elif pc == 2:
    if jogador == 0:
        print("VOCÊ GANHOU!")
    elif jogador == 1:
        print("VOCÊ PERDEU!")
    elif jogador == 2:
        print("JOGO EMPATADO!")
    else: 
        print("JOGADA INVÁLIDA!!!")