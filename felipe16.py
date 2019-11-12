from datetime import date
hoje = date.today().year
total_maior = 0
total_menor = 0
for c in range(1,5):
    ano = int(input(("Em que ano a {}ª pessoa nasceu? ".format(c))))
    idade = hoje - ano
    if idade < 18:
        total_menor += 1
    else:
        total_maior += 1    
print("Ao todo temos {} pessoas maiores de idade e {} pessoas menores de idade.".format(total_maior, total_menor))