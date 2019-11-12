print("--------CADASTRO DE PESSOAS---------")
maiores = tot20 = totH = pessoas = 0
while True:
    pessoas += 1
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]
    while sexo not in "MFmf":
        sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]
    if idade >= 18:
        maiores += 1
    if sexo in "F" and idade < 20:
        tot20 += 1 
    if sexo in "M":
        totH +=1
    resp = " "    
    while resp not in "SN":
        resp = str(input("QUER CONTINUAR? [S/N] ")).upper().strip()[0]
    if resp in "N":
        print("--------O PROGRAMA ENCERROU.--------")
        break
print(f"No total, {pessoas} pessoas foram registradas, existem {maiores} pessoas maiores de idade.")
print(f"Foram cadastradas {tot20} mulheres com menos de 20 anos.")
print(f"Foram cadastrados {totH} homens.")

