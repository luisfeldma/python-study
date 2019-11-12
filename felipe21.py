from random import randint
n1 = randint(0, 20)
print("Um número entre 0 e 20 foi selecionado.")
n2 = int(input("Advinhe qual é o número: "))
palpites = 1
while n2 != n1:
    palpites += 1
    if n2 > n1:
        n2 = int(input("Errou... Chute um número MENOR: "))
    else:
        n2 = int(input("Errou... Chute um número MAIOR: "))
if n2 == n1:
    print("Parabéns! Você acertou! Você levou {} tentativas.".format(palpites))    
