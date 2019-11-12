soma_idade = 0
nomevelho = 0
totmulher20 = 0
maioridadehomem = 0
num_pessoas = 5
for info in range(1, num_pessoas + 1):
    print("------{}ª PESSOA------".format(info))
    nome = str(input("Nome: ")).capitalize().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    soma_idade += idade
    if info == 1 and sexo in "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "F" and idade < 20:
        totmulher20 += 1     

print("A média das idades é de: {:.2f} anos.".format(soma_idade / info)) 
print("O homem mais velho se chama {}, e tem {} anos.".format(nomevelho, maioridadehomem))
print("Existe(m) {} mulher(es) com menos de 20 anos.".format(totmulher20))
   
