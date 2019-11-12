print("-------BANCO DO BRASIL-------")
valor = int(input("Qual valor você quer sacar? R$ "))
tot100 = tot50 = tot20 = tot10 = 0
ced100 = 100
ced50 = 50
ced20 = 20
ced10 = 10
while valor >= 300:
    valor -= ced100
    tot100 += 1
while valor > 50:
    valor -= ced50
    tot50 += 1 
while valor > 10:
    valor -= ced20
    tot20 += 1
while valor != 0:
    valor -= ced10
    tot10 += 1    
print(f"""Você resgatará:
{tot100} notas de 100
{tot50} notas de 50
{tot20} notas de 20
{tot10} notas de 10.""")       