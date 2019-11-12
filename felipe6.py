import random
pc = random.randint(0, 5)
print("Vou pensar em um número de 0 a 5, e te desafio a acertar qual é esse número..")
print(" ")
chute = int(input("Qual número eu pensei? "))
print(" ")
print("Analisando seu chute...")
print(" ")
if chute == pc:
    print("Parabéns! Você acertou!")
else:
    print("Que pena... Tente novamente.")    
