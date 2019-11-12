from time import sleep
from random import randint
print("-----------Jogo do par ou ímpar!------------")
cont = 0
while True:
    print("""Escolha :
    [0] PAR
    [1] ÍMPAR""")
    opção = int(input("Qual é sua opção? "))
    while opção > 1:
        print("Opção inválida! Escolha [0] para 'par' e [1] para 'ímpar'.")
        opção = int(input("Qual é sua opção? ")) 
    n_pc = randint(1, 5)
    n_jg = int(input("Escolha um número de 1 a 5: "))
    while n_jg > 5:
        print("Número inválido! Escolha um número entre 1 e 5!")
        n_jg = int(input("Escolha um número de 1 a 5: "))
    cont += 1
    soma = n_jg + n_pc
    sleep(0.5)
    print("--" * 15)
    print(f"O PC escolheu {n_pc} e você escolheu {n_jg}.")
    if opção == 0 and soma % 2 == 0 or opção == 1 and soma % 2 != 0:
        print("--------VOCÊ GANHOU!--------")
    else:
        print(f"VOCÊ PERDEU! VOCÊ JOGOU {cont} VEZ(ES).")
        break
sleep(10)        
       


