from datetime import date
ano = int(input("Digite o ano de seu nascimento: "))
hj = date.today().year
if hj - ano > 18 :
    qu = str(input("Você já se alistou? ")).capitalize()
    if "Sim" in qu :
        print("Ok, está tudo bem!")
    else :
        print("Se dirija à unidade militar mais próxima de sua residência o quanto antes!")
        print("Você está {} ano(s) atrasado.".format((hj - ano) - 18))
elif hj - ano < 18 :
    print("Você ainda não precisa se alistar esse ano.")
    print("Se aliste daqui a {} ano(s).".format(18 - (hj - ano)))
else :
    print("Você precisa se alistar esse ano! Se dirija à unidade militar mais próxima de sua casa.")




    