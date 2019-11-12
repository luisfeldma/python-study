from datetime import date
ano = int(input("Digite o ano de seu nascimento: "))
hj = date.today().year
idade = hj - ano 
if idade <= 9 :
    print("Você está na categoria MIRIM!")
elif 9 < idade <= 14 :
    print("Você está na categoria INFANTIL!")
elif 14 < idade <= 19 :
    print("Você está na categoria JUNIOR!")
elif 19 < idade <= 20 :
    print("Você está na categoria SÊNIOR!")    
else :
    print("Você está na categoria MASTER!") 