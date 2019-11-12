sexo = str(input("SEXO [M/F]: ")).upper().strip()[0]
while sexo not in "MmFf":
    sexo = str(input("Dado inválido. Digite seu sexo [M/F] novamente: ")).strip().upper()[0]  
print("Sexo {} registrado com sucesso.".format(sexo))      
    